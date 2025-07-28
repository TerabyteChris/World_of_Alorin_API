import openai
import tiktoken
import google.generativeai as genai
import time
import asyncio
from openai import OpenAI, OpenAIError
from fastapi import FastAPI, HTTPException, APIRouter, Request, Body, Query, BackgroundTasks, Header, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import Limiter as SlowapiLimiter
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, PlainTextResponse
from typing import List, Dict
from difflib import get_close_matches
from storage import load_history, save_message, update_last_summarized_token_usage
from pydantic import BaseModel
from typing import List, Optional
from pathlib import Path
import os, json, logging, traceback
from datetime import datetime
import re
import uuid
from uuid import uuid4
import httpx
from fastapi.responses import JSONResponse
from models import NPC, Location, Faction  # Only import the class definitions here
from save_file_models import SaveFile
from npc_data import raw_npcs  # Your validated NPC instances
from location_data import raw_locations
from faction_data import raw_factions
from thread_store import add_thread_entry, list_threads, load_thread_store
from token_tracker import add_token_usage, get_token_usage
from thread_registry import get_or_create_thread_id_by_session
from merge_save_files import merge_save_files
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.WARNING)



OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
ASSISTANT_ID = os.getenv("OPENAI_ASSISTANT_ID")
openai.timeout = 30
ENCODER = tiktoken.encoding_for_model("gpt-4o")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_KEYS = {GEMINI_API_KEY} if GEMINI_API_KEY else set()




app = FastAPI(title="World of Alorin API", version="1.2")
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
save_router = APIRouter()

app.state.gemini_model = genai.GenerativeModel("gemini-2.5-pro")


origins = [
    "https://alorinworld.com", # <-- replace with your app domain once deployed
    ]


 
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["GET", "POST"],
   allow_headers=["Authorization", "Content-Type", "x-api-key"],
   )



# === Utility ===
def to_slug(name: str) -> str:
    return re.sub(r'\W+', '-', name.strip().lower())
    

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid or missing API key") 


# === NPC Loader ===
npcs: Dict[str, NPC] = {}

for name, data in raw_npcs.items():
    try:
        slug = to_slug(name)
        aliases = set(data.aliases or [])
        aliases.add(name)
        aliases.add(slug)
        data.aliases = list(aliases)
        npcs[slug] = data
    except Exception as ex:
        logging.error(f"Error loading NPC '{name}': {ex}")

# === Location Loader ===
locations: Dict[str, Location] = {}

for name, data in raw_locations.items():
    try:
        slug = to_slug(name)
        locations[slug] = data
    except Exception as ex:
        logging.error(f"Error loading location '{name}': {ex}")

# === Faction Loader ===
factions: Dict[str, Faction] = {}

for name, data in raw_factions.items():
    try:
        slug = to_slug(name)
        factions[slug] = data
    except Exception as ex:
        logging.error(f"Error loading location '{name}': {ex}")



def wait_for_run_complete(thread_id, run_id, timeout=60, poll_interval=2):
    """
    Polls the run status until completion or timeout.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
        if run_status.status == "completed":
            return run_status
        elif run_status.status in {"failed", "cancelled", "expired"}:
            raise RuntimeError(f"Run failed with status: {run_status.status}")
        time.sleep(poll_interval)
    raise TimeoutError("Timed out waiting for run to complete.")


def estimate_tokens(text: str) -> int:
    # Rough heuristic: 1 token ≈ 4 characters
    return len(text) // 4



def safe_parse_json(raw_text: str):
    # Remove triple backticks or language hints like ```json
    clean = re.sub(r"```(?:json)?", "", raw_text.strip(), flags=re.IGNORECASE)
    try:
        return json.loads(clean)
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON: {e}")
        return {}




def chunk_text_by_tokens(text: str, token_limit: int) -> list[str]:
    """Splits text into chunks that do not exceed token_limit."""
    import tiktoken  # or your tokenizer of choice
    encoding = tiktoken.encoding_for_model("gpt-4")  # or your model
    tokens = encoding.encode(text)

    chunks = []
    start = 0
    while start < len(tokens):
        end = start + token_limit
        chunk = encoding.decode(tokens[start:end])
        chunks.append(chunk)
        start = end

    return chunks

def prune_known_locations_safe(locations, campaign, npcs):
    used_locations = set()

    # Normalize and gather names
    def norm(text):
        return text.strip().lower() if isinstance(text, str) else ""

    # 1. Current location
    current_loc = norm(campaign.get("current_location"))
    if current_loc:
        used_locations.add(current_loc)

    # 2. From quests
    for quest in campaign.get("active_quests", []):
        desc = norm(quest.get("description", ""))
        for loc in locations:
            if norm(loc.get("name")) in desc:
                used_locations.add(norm(loc.get("name")))

    # 3. From NPC presence
    npc_names = {norm(npc.get("name")) for npc in npcs}
    for loc in locations:
        for npc_name in loc.get("npcs_present", []):
            if norm(npc_name) in npc_names:
                used_locations.add(norm(loc.get("name")))

    # 4. Prune unused locations
    for loc in locations:
        loc_name = norm(loc.get("name"))
        if loc_name not in used_locations:
            for key in loc.keys():
                if key not in ("name", "history"):
                    loc[key] = None


def collapse_logs(logs: list[str], keep_last: int = 3) -> list[str]:
    if not isinstance(logs, list) or len(logs) <= keep_last + 1:
        return logs

    combined_text = "; ".join(log[:120].strip() for log in logs[:-keep_last])
    merged = f"Earlier sessions involved: {combined_text}."
    return [merged] + logs[-keep_last:]



def narrativize_summary(summary_cache: dict) -> str:
    if not isinstance(summary_cache, dict):
        return ""

    lines = []

    # === Player Character ===
    pc = summary_cache.get("player_character", {})
    if pc:
        lines.append("Player Character:")
        lines.append(f"{pc.get('name', 'Unknown')}, a level {pc.get('level', '?')} {pc.get('race', '')} {pc.get('character_class', '')}.")
        if pc.get("background"):
            lines.append(f"Background: {pc['background']}")
        if pc.get("alignment"):
            lines.append(f"Alignment: {pc['alignment']}")
        if pc.get("appearance"):
            lines.append(f"Appearance: {pc['appearance']}")
        if pc.get("notable_traits"):
            lines.append(f"Notable Traits: {pc['notable_traits']}")
        if pc.get("features"):
            lines.append(f"Features: {pc['features']}")
        if pc.get("traits"):
            lines.append(f"Traits: {pc['traits']}")
        if pc.get("ideals"):
            lines.append(f"Ideals: {pc['ideals']}")
        if pc.get("bonds"):
            lines.append(f"Bonds: {pc['bonds']}")
        if pc.get("flaws"):
            lines.append(f"Flaws: {pc['flaws']}")
        if pc.get("backstory"):
            lines.append(f"Backstory: {pc['backstory']}")
        lines.append("")

        # Mechanical stats
        stats = [
            ("HP", f"{pc.get('current_hp', '?')}/{pc.get('max_hp', '?')}"),
            ("AC", pc.get("armor_class")),
            ("Initiative", pc.get("initiative")),
            ("Speed", pc.get("speed")),
            ("Passive Perception", pc.get("passive_perception"))
        ]
        lines.append("Stats: " + ", ".join(f"{k}: {v}" for k, v in stats if v is not None))

        if pc.get("ability_scores"):
            lines.append("Ability Scores:")
            for ability, score in pc["ability_scores"].items():
                val = score.get("score", "?")
                mod = score.get("mod", "?")
                lines.append(f"  {ability}: {val} (mod {mod})")

        if pc.get("saving_throws"):
            lines.append(f"Saving Throws: {', '.join(pc['saving_throws'])}")
        if pc.get("skills"):
            lines.append(f"Skills: {', '.join(pc['skills'])}")
        if pc.get("hit_dice"):
            lines.append(f"Hit Dice: {pc['hit_dice']}")
        if pc.get("death_saves"):
            lines.append(f"Death Saves: {pc['death_saves']}")
        if pc.get("attacks_and_spellcasting"):
            lines.append(f"Attacks & Spellcasting: {pc['attacks_and_spellcasting']}")
        if pc.get("spells"):
            lines.append(f"Spells Known: {', '.join(pc['spells'])}")
        if pc.get("spell_slots"):
            lines.append("Spell Slots:")
            for lvl, slots in pc["spell_slots"].items():
                lines.append(f"  Level {lvl}: {slots} slots")
        if pc.get("inventory"):
            lines.append(f"Inventory: {', '.join(pc['inventory'])}")
        if pc.get("currency"):
            lines.append("Currency:")
            for coin, amount in pc["currency"].items():
                lines.append(f"  {coin}: {amount}")
        lines.append("")

    # === Key NPCs ===
    npcs = summary_cache.get("key_npcs", [])
    if npcs:
        lines.append("Key NPCs:")
        for npc in npcs:
            name = npc.get("name", "Unnamed")
            desc = npc.get("description", "No description")
            lines.append(f"- {name}: {desc}")

            # === Relationship Subfields
            relationship = npc.get("relationship", {})
            if relationship:
                trust_level = relationship.get("trust_level", "N/A")
                current_status = relationship.get("current_status")
                history = relationship.get("history")

                lines.append(f"  Relationship:")
                lines.append(f"    Trust Level: {trust_level}")
                if current_status:
                    lines.append(f"    Current Status: {current_status}")
                if history:
                    lines.append(f"    History: {history}")


            # === Other NPC metadata
            if npc.get("role"):
                lines.append(f"  Role: {npc['role']}")
            if npc.get("motives_or_secrets"):
                lines.append(f"  Motives: {npc['motives_or_secrets']}")
            if npc.get("known_alliances"):
                lines.append(f"  Known Alliances: {npc['known_alliances']}")
            if npc.get("known_enemies"):
                lines.append(f"  Known Enemies: {npc['known_enemies']}")
            if npc.get("goals"):
                lines.append(f"  Goals: {npc['goals']}")
            if npc.get("times_met") is not None:
                lines.append(f"  Times Met: {npc['times_met']}")
            notes = npc.get("interaction_notes", [])
            if notes:
                lines.append("  Interaction Notes:")
                for note in notes:
                    lines.append(f"    - {note}")

        lines.append("")

    # === Factions ===
    factions = summary_cache.get("factions_encountered", [])
    if factions:
        lines.append("Factions Encountered:")
        for faction in factions:
            lines.append(f"- {faction['name']}: {faction.get('goals', 'No known goals')}")
            
            if faction.get("interaction_summary"):
                lines.append(f"  Summary: {faction['interaction_summary']}")
            
            if faction.get("times_encountered") is not None:
                lines.append(f"  Times Encountered: {faction['times_encountered']}")

            notes = faction.get("interaction_notes", [])
            if notes:
                lines.append("  Interaction Notes:")
                for note in notes:
                    lines.append(f"    - {note}")
        lines.append("")


    # === Locations ===
    locations = summary_cache.get("known_locations", [])
    if locations:
        lines.append("Known Locations:")
        for loc in locations:
            lines.append(f"- {loc['name']}: {loc.get('description', 'No description available')}")
            if loc.get("key_features"):
                lines.append(f"  Features: {', '.join(loc['key_features'])}")
            if loc.get("npcs_present"):
                lines.append(f"  NPCs Present: {', '.join(loc['npcs_present'])}")
            if loc.get("factions_present"):
                lines.append(f"  Factions Present: {', '.join(loc['factions_present'])}")
            if loc.get("history"):
                lines.append(f"  History: {loc['history']}")
        lines.append("")

    # === Campaign State ===
    campaign = summary_cache.get("campaign", {})
    if campaign:
        lines.append("Campaign State:")

        if campaign.get("current_location"):
            lines.append(f"  Current Location: {campaign['current_location']}")

        if campaign.get("current_situation"):
            lines.append(f"  Situation: {campaign['current_situation']}")

        if campaign.get("world_state"):
            lines.append(f"  World State: {campaign['world_state']}")

        if campaign.get("world_modifiers"):
            lines.append(f"  World Modifiers: {', '.join(campaign['world_modifiers'])}")

        if campaign.get("summary_of_events"):
            lines.append("  Event Summary:")
            for item in campaign["summary_of_events"]:
                lines.append(f"    - {item}")

        if campaign.get("session_notes"):
            lines.append("  Session Notes:")
            for note in campaign["session_notes"]:
                lines.append(f"    - {note}")

        if campaign.get("player_decisions"):
            lines.append("  Notable Decisions:")
            for decision in campaign["player_decisions"]:
                lines.append(f"    - {decision}")

        if campaign.get("inventory_and_equipment"):
            lines.append("  Equipment:")
            for item in campaign["inventory_and_equipment"]:
                lines.append(f"    - {item}")

        if campaign.get("campaign_variables"):
            lines.append("  Campaign Variables:")
            for var in campaign["campaign_variables"]:
                lines.append(f"    - {var}")

        if campaign.get("ongoing_objectives"):
            lines.append("  Objectives:")
            for obj in campaign["ongoing_objectives"]:
                lines.append(f"    - {obj}")

        if campaign.get("active_quests"):
            lines.append("  Active Quests:")
            for quest in campaign["active_quests"]:
                lines.append(f"    - {quest['title']}: {quest.get('description', '')} (Status: {quest.get('status', 'Unknown')})")

                if quest.get("key_decisions"):
                    lines.append(f"      Key Decisions:")
                    for decision in quest["key_decisions"]:
                        lines.append(f"        - {decision}")

        lines.append("")


    # === Session Chunks (optional summaries) ===
    session_chunks = summary_cache.get("session_chunks")
    if session_chunks:
        lines.append("Session Recaps:")
        for i, chunk in enumerate(session_chunks[-3:], 1):  # Show last 3 chunks
            lines.append(f"  Recap {i}: {chunk}")
        lines.append("")

    return "\n".join(lines).strip()



# === Endpoints ===
@app.post("/api/gemini/chat")
@limiter.limit("12/minute")  # or "100/hour" etc.
async def chat_with_gemini(
    request: Request,
    api_key: str = Depends(verify_api_key)  # 🔒 Enforces API key
):
    try:
        gemini_model = request.app.state.gemini_model

        data = await request.json()
        prompt = data.get("prompt", "").strip()
        thread_id = data.get("thread_id") or str(uuid4())
        system_instruction = data.get("system_instruction", "").strip()
        bootstrap_memory = data.get("bootstrap_memory")


        if not prompt:
            return JSONResponse(status_code=400, content={"error": "Missing prompt"})


        # === Load history
        history, _ = load_history(thread_id)
        save_message(thread_id, "user", prompt)

        # === Load summary_cache, SaveFile, and startup flag
        summary_cache = None
        savefile_json = None
        startup_script = None
        startup_injected = False
        last_summarized_token_usage = 0
        save_path = os.path.join("./saves", f"{thread_id}.json")

        if os.path.exists(save_path):
            with open(save_path, "r", encoding="utf-8") as f:
                save_data = json.load(f)
                summary_cache = save_data.get("summary_cache") or None
                savefile_json = json.dumps(save_data, indent=2)
                startup_injected = save_data.get("startup_injected", False)
                last_summarized_token_usage = save_data.get("last_summarized_token_usage", 0)


            # Inject startup script if needed
            if summary_cache and not startup_injected:
                with open("./prompts/startup_script.txt", "r", encoding="utf-8") as f:
                    startup_script = f.read().strip()
                save_data["startup_injected"] = True
                with open(save_path, "w", encoding="utf-8") as f:
                    json.dump(save_data, f, indent=2)

        elif bootstrap_memory:
            # ✅ First-time SaveFile creation via bootstrap
            summary_cache = bootstrap_memory
            savefile_json = json.dumps(bootstrap_memory, indent=2)

            # Read startup script for first message
            with open("./prompts/startup_script.txt", "r", encoding="utf-8") as f:
                startup_script = f.read().strip()

            payload = {
                "thread_id": thread_id,
                "summary_cache": bootstrap_memory,
                "timestamp": datetime.utcnow().isoformat(),
                "last_summarized_token_usage": 0,
                "token_usage": 0,
                "startup_injected": True
            }
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2)

        # === Build full prompt safely
        full_prompt_parts = []

        if system_instruction:
            full_prompt_parts.append(f"System: {system_instruction}")
            
        
        if startup_script:
            full_prompt_parts.append("Narrative Intro:\n" + startup_script)
            

        if summary_cache:
            narrativized = narrativize_summary(summary_cache)
            full_prompt_parts.append("Summary Cache:\n" + narrativized)


        if savefile_json:
            savefile_dict = json.loads(savefile_json)
            full_prompt_parts.append("Save File:\n" + narrativize_summary(savefile_dict))



        # === Determine which messages have not been summarized
        unsummarized_turns = []
        cumulative_tokens = 0
        for message in history:
            cumulative_tokens += message.get("token_usage", 0)
            if cumulative_tokens > last_summarized_token_usage:
                unsummarized_turns.append(message)

        # === Add only unsummarized messages to the prompt
        formatted_turns = [
            f"{m['role'].capitalize()}: {m['content']}"
            for m in unsummarized_turns
        ]
        full_prompt_parts.extend(formatted_turns)


        full_prompt_parts.append(f"Player: {prompt}")
        full_prompt = "\n\n".join(full_prompt_parts).strip()

        # === Token tracking
        token_info = gemini_model.count_tokens(full_prompt)
        token_count = token_info.total_tokens if token_info else 0
        
        # === Debug summary/narrative memory
        #if summary_cache:
            #print("📦 summary_cache (JSON preview):")
            #print(json.dumps(summary_cache, indent=2))

            #print("📝 Narrativized summary_cache (preview):")
            #print(narrativize_summary(summary_cache))  

        #elif savefile_json:
            #savefile_dict = json.loads(savefile_json)
            #print("📦 savefile_json (JSON preview):")
            #print(json.dumps(savefile_dict, indent=2))

            #print("📝 Narrativized savefile_json (preview):")
            #print(narrativize_summary(savefile_dict))   


        # === Logging
        #print("📝 Final prompt preview (first 1000 chars):")
        print("=== SUMMARY CACHE INCLUDED ===" if summary_cache else "=== NO SUMMARY CACHE ===")
        print("=== SAVEFILE JSON INCLUDED ===" if savefile_json else "=== NO SAVEFILE JSON ===")
        print("FULL PROMPT START")
        print(full_prompt)
        print("FULL PROMPT END")
        #print(f"🧮 Prompt token count: {token_count}")
        #print(f"🧾 Prompt length (chars): {len(full_prompt)}")
        #print(f"📏 Prompt part count: {len(full_prompt_parts)}")
        #print(f"🧮 Using summary_cache? {'✅' if summary_cache else '❌'}")

        # === Send to Gemini
        chat = gemini_model.start_chat()
        response = chat.send_message(full_prompt)
        reply = response.text.strip()

        # === Token tracking: reply
        reply_token_info = gemini_model.count_tokens(reply)
        reply_token_count = reply_token_info.total_tokens if reply_token_info else 0

        # === Total token usage
        total_tokens = token_count + reply_token_count

        # === Save reply
        save_message(thread_id, "gemini", reply, token_usage=total_tokens)

        return {
            "response": reply,
            "thread_id": thread_id,
            "token_usage": total_tokens
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})






def get_total_tokens(thread_id: str, current_tokens: int = 0) -> int:
    """
    Returns the total tokens used in a thread, including saved history and optional current count.
    
    Parameters:
    - thread_id (str): The thread/session ID
    - current_tokens (int): Tokens used in the current request (default: 0)
    
    Returns:
    - int: Cumulative token usage for the thread
    """
    try:
        history, _ = load_history(thread_id)
    except Exception:
        history = []

    saved_total = sum(
        m.get("token_usage", 0)
        for m in history
        if m["role"] in ("user", "gemini")
    )

    return saved_total + current_tokens




CHUNK_SIZE = 25000  # character-based chunk size

def chunk_transcript(transcript: str, max_chars: int = CHUNK_SIZE) -> List[str]:
    return [transcript[i:i + max_chars] for i in range(0, len(transcript), max_chars)]

async def summarize_chat_history_with_gemini(gemini_model, thread_id: str) -> str:
    try:
        # === Load chat history (assumes load_history returns list of { role, content })
        messages, _ = load_history(thread_id)
        if not messages:
            raise HTTPException(status_code=400, detail="No chat history to summarize")

        # === Build transcript
        transcript = "\n\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in messages)

        # === Chunk transcript
        chunks = chunk_transcript(transcript)

        summaries = []
        for i, chunk in enumerate(chunks):
            print(f"📦 Summarizing chunk {i + 1} of {len(chunks)}...")

            prompt = f"""You are a memory assistant for a solo Dungeons & Dragons campaign.

Summarize the transcript below into a **compact, structured memory record**. Prioritize:

- Key player actions and choices
- Major NPCs and evolving relationships
- Emotional tone, goals, and unresolved threads
- Relevant world or factional developments

Avoid:
- Long-form storytelling
- Full dialogue
- Rich narrative tone or literary voice

Use a bullet list or short paragraphs. Make sure to include enough information to populate the current full Character sheet in your summary: 
Character Name: [Name]
Race/Species: [Race]
Class & Level: [Class] [Level]
Background: [Background]
Alignment: [Alignment]
Experience Points: [XP]

Ability Scores:
Strength: [Score] ([Mod])
Dexterity: [Score] ([Mod])
Constitution: [Score] ([Mod])
Intelligence: [Score] ([Mod])
Wisdom: [Score] ([Mod])
Charisma: [Score] ([Mod])

Saving Throws: [List]
Skills: [List]
Passive Perception: [Value]

Combat Stats:
Armor Class: [AC]
Initiative: [Value]
Speed: [Value]
Hit Points: [HP]
Hit Dice: [Type]
Death Saves: [Status]

Attacks & Spellcasting: [Summary]

Inventory:
Equipment: [List]
Currency: [Amounts]

Spells:
[List if applicable]

Roleplaying Info:
Traits, Ideals, Bonds, Flaws
Features, Appearance, Backstory. This memory will be sent to an AI model to retain context in future sessions.

Transcript:
{chunk}

"""
            chat = gemini_model.start_chat()
            response = chat.send_message(prompt)
            summary = response.text.strip()

            summaries.append(f"📍 Summary Part {i + 1}:\n{summary}")

        full_summary = "\n\n".join(summaries)
        return full_summary

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Gemini summarization failed.")



@app.get("/api/gemini/sessions")
async def list_gemini_sessions(api_key: str = Depends(verify_api_key)):
    path = os.path.join("data", "gemini_sessions.json")
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            registry = json.load(f)
        return list(registry.keys())
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})




@app.post("/api/gemini/session")
async def get_or_create_gemini_thread(request: Request, api_key: str = Depends(verify_api_key)):
    data = await request.json()
    session_name = data.get("session_name", "").strip()

    if not session_name:
        return JSONResponse(status_code=400, content={"error": "Missing session name"})

    thread_id = get_or_create_thread_id_by_session(session_name)
    return { "thread_id": thread_id }
    
    

@app.get("/api/gemini/thread/{thread_id}")
async def get_thread_history(thread_id: str, api_key: str = Depends(verify_api_key)):
    try:
        history, _ = load_history(thread_id)
        return { "messages": history }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})





SAVE_DIR = "./saves"
os.makedirs(SAVE_DIR, exist_ok=True)

client = OpenAI()


@save_router.patch("/save/{thread_id}")
async def patch_player_data(
    thread_id: str,
    player_patch: dict = Body(...),
    api_key: str = Depends(verify_api_key)
):
    path = os.path.join("saves", f"{thread_id}.json")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="SaveFile not found")

    with open(path, "r", encoding="utf-8") as f:
        save_data = json.load(f)

    # Apply patch to the player_character section
    player_data = save_data.get("summary_cache", {}).get("player_character", {})
    for key, val in player_patch.items():
        player_data[key] = val  # Only updates what is passed

    # Save back the updated structure
    with open(path, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=2)

    return {"message": "Player character data updated successfully."}





class ThreadSaveRequest(BaseModel):
    session_id: str
    thread_id: str

@app.post("/threads/store")
async def store_thread(info: ThreadSaveRequest, api_key: str = Depends(verify_api_key)):
    try:
        add_thread_entry(session_id=info.session_id, thread_id=info.thread_id)
        logging.info(f"[Thread Store] Stored thread {info.thread_id} for session {info.session_id}")
        return {"message": "Thread stored."}
    except Exception as e:
        logging.error("[Thread Store] Failed")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to store thread")



@app.get("/threads/lookup/{thread_id}")
async def lookup_session_name(thread_id: str, api_key: str = Depends(verify_api_key)):
    store = load_thread_store()
    print(f"[LOOKUP] thread_id requested: {thread_id}")
    print(f"[LOOKUP] store contents: {store}")
    for entry in store:
        if entry["thread_id"] == thread_id:
            print(f"[FOUND] {entry}")
            return {"session_id": entry["session_id"]}
    raise HTTPException(status_code=404, detail="Thread not found")



def count_tokens(text: str) -> int:
    return len(ENCODER.encode(text))


def get_trimmed_summary_chunks(save_file: SaveFile, token_limit: int = 10000) -> List[str]:
    """
    Extracts chunked narrative blocks from summary_cache, returns as many chunks
    as fit within the given token limit.
    """
    if not save_file.summary_cache:
        return []

    raw_chunks = save_file.summary_cache.strip().split("\n---\n")
    selected_chunks = []
    token_total = 0

    for chunk in raw_chunks:
        chunk = chunk.strip()
        tokens = count_tokens(chunk)
        if token_total + tokens > token_limit:
            break
        selected_chunks.append(chunk)
        token_total += tokens

    return selected_chunks


def chunk_text(text: str, max_tokens: int = 25000) -> list:
    lines = text.split("\n")
    chunks = []
    current_chunk = []
    current_tokens = 0

    for line in lines:
        token_count = count_tokens(line)
        if current_tokens + token_count > max_tokens:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_tokens = 0

        current_chunk.append(line)
        current_tokens += token_count

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks



def estimate_tokens(text: str) -> int:
    # Rough heuristic: 1 token ≈ 4 characters
    return len(text) // 4


COOLDOWN_SECONDS = 180  # Customize: how long to wait before allowing another run

def is_summary_locked(thread_id):
    lock_path = Path(f"locks/summarize_{thread_id}.lock")
    if not lock_path.exists():
        return False
    return (time.time() - lock_path.stat().st_mtime) < COOLDOWN_SECONDS

def set_summary_lock(thread_id):
    lock_path = Path(f"locks/summarize_{thread_id}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path.touch()

def clear_summary_lock(thread_id):
    try:
        Path(f"locks/summarize_{thread_id}.lock").unlink(missing_ok=True)
    except Exception as e:
        print(f"⚠️ Failed to clear lock for {thread_id}: {e}")



def summarize_in_background(gemini_model, thread_id):
    if is_summary_locked(thread_id):
        print(f"⚠️ Summary already running or recently finished for thread {thread_id}. Skipping.")
        return

    set_summary_lock(thread_id)

    try:
        print(f"🧠 Starting background summarization for thread: {thread_id}")

        # === Load chat history
        messages, _ = load_history(thread_id)
        if not messages:
            print(f"❌ No messages to summarize for thread {thread_id}")
            return

        # === Flatten full transcript
        full_transcript = "\n\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in messages)

        # === Load previous SaveFile (if exists)
        previous_summary = None
        save_path = os.path.join("saves", f"{thread_id}.json")

        if os.path.exists(save_path):
            with open(save_path, "r", encoding="utf-8") as f:
                previous_data = json.load(f)
                previous_summary = previous_data.get("summary_cache")

        previous_summary_json = json.dumps(previous_summary, indent=2) if previous_summary else "null"

        # === Step 1: Generate structured SaveFile JSON
        savefile_prompt = f"""
This is the most recent campaign save state, which may be incomplete or outdated:
{previous_summary_json}

Below is the complete chat transcript for the current session:
{full_transcript}

Goal: Generate a new SaveFile JSON that:

Accurately reflects all developments to date in the campaign.

Preserves prior information unless clearly contradicted or made obsolete.

Merges new details with existing data to ensure narrative and mechanical continuity.

Instructions:

Merge, don’t overwrite:

Append to arrays like interaction_notes, session_notes, player_decisions, etc.

Update scalar and nested fields (e.g., current_hp, trust_level, relationship, status) only if new information provides additional, clearer, or more recent detail.

For relationship objects (e.g., within NPCs), update current_status and trust_level if player interactions suggest a shift in tone, loyalty, or attitude. Extend or revise history if meaningful past context is added. Always append to interaction_notes if new interactions are present.

Prioritize the transcript as the authoritative source in case of contradiction.

Do not remove any previously recorded NPCs, factions, quests, or known locations.

Redundancy is acceptable; data loss is not. Merge partial updates with previously saved content.

NPCs:

Always include existing and newly introduced NPCs.

Merge per-NPC details where new data adds or clarifies existing fields.

Never remove or replace established NPCs.

Each must include: name, description, role, known_alliances, known_enemies, motives_or_secrets, relationship, times_met, and at least one interaction_note.

Factions:

Include all previously encountered or currently relevant factions.

Merge updated goals, summaries, and interactions with existing faction records.

Each must include: name, goals, interaction_summary, times_encountered, and at least one interaction_note.

Active Quests:

Retain all previously active quests unless explicitly completed or abandoned.

Merge new quest developments and player actions into existing quest entries.

Each must include: title, description, status, and 1–3 concise key_decisions.

Output Format:
Reply only with pure JSON matching the exact schema below. Do not include any commentary, markdown, or formatting.
(Use null or omit optional fields if unknown.)
{{
  "session_id": "<string>",
  "timestamp": "<ISO 8601 datetime string>",
  "player_character": {{
    "name": "<string>",
    "character_class": "<string>",
    "race": "<string>",
    "background": "<string>",
    "level": <int>,
    "alignment": "<string>",
    "max_hp": <int>,
    "current_hp": <int>,
    "initiative": <int>,
    "armor_class": <int>,
    "speed": <int>,
    "hit_dice": "<string>",
    "death_saves": "<string>",
    "ability_scores": {{
      "Strength": {{ "score": <int>, "mod": <int> }},
      "Dexterity": {{ "score": <int>, "mod": <int> }},
      "Constitution": {{ "score": <int>, "mod": <int> }},
      "Intelligence": {{ "score": <int>, "mod": <int> }},
      "Wisdom": {{ "score": <int>, "mod": <int> }},
      "Charisma": {{ "score": <int>, "mod": <int> }}
    }},
    "saving_throws": ["<string>"],
    "skills": ["<string>"],
    "passive_perception": <int>,
    "spell_slots": {{ "1": <int>, "2": <int> }},
    "spells": ["<string>"],
    "attacks_and_spellcasting": "<string>",
    "inventory": ["<string>"],
    "currency": {{ "gp": <int>, "sp": <int>, "cp": <int> }},
    "traits": "<string>",
    "ideals": "<string>",
    "bonds": "<string>",
    "flaws": "<string>",
    "features": "<string>",
    "appearance": "<string>",
    "backstory": "<string>",
    "notable_traits": "<string>"
  }},
  "key_npcs": [
    {{
      "name": "<string>",
      "description": "<string>",
      "role": "<string>",
      "known_alliances": "<string>",
      "known_enemies": "<string>",
      "motives_or_secrets": "<string>",
      "relationship": {{
        "history": "<string>",
        "current_status": "<string>",
        "trust_level": <int>
      }},
      "times_met": <int>,
      "interaction_notes": ["<string>"]
    }}
  ],
  "known_locations": [
    {{
      "name": "<string>",
      "description": "<string>",
      "key_features": ["<string>"],
      "npcs_present": ["<string>"],
      "factions_present": ["<string>"],
      "history": "<string>"
    }}
  ]
  "factions_encountered": [
    {{
      "name": "<string>",
      "goals": "<string>",
      "interaction_summary": "<string>",
      "times_encountered": <int>,
      "interaction_notes": ["<string>"]
    }}
  ],
  "campaign": {{
    "summary_of_events": ["<string>"],
    "world_state": "<string>",
    "world_modifiers": ["<string>"],
    "session_notes": ["<string>"],
    "player_decisions": ["<string>"],
    "ongoing_objectives": ["<string>"],
    "inventory_and_equipment": ["<string>"],
    "campaign_variables": ["<string>"],
    "current_location": "<string>",
    "current_situation": "<string>",
    "active_quests": [
      {{
        "title": "<string>",
        "description": "<string>",
        "status": "<string>",
        "key_decisions": ["<string>"]
      }}
    ]
  }}
}}
"""

        savefile_response = gemini_model.generate_content(savefile_prompt)
        savefile_response_text = savefile_response.text.strip()

        # Token tracking
        savefile_prompt_tokens = estimate_tokens(savefile_prompt)
        savefile_response_tokens = estimate_tokens(savefile_response_text)

        raw_json = safe_parse_json(savefile_response_text)
        save_data = raw_json if isinstance(raw_json, dict) else {}

        # === Post-parse validation of NPC data
        for npc in save_data.get("key_npcs", []):
            name = npc.get("name", "UNKNOWN")
            if "times_met" not in npc or npc["times_met"] is None:
                print(f"⚠️ NPC missing times_met: {name}")
            if not npc.get("interaction_notes"):
                print(f"⚠️ NPC missing interaction_notes: {name}")

        save_json = json.dumps(save_data, indent=2)
        
        campaign = save_data.get("campaign", {})

        # === Prune if over token budget
        if estimate_tokens(save_json) > 12000:
            print("⚠️ SaveFile exceeds token budget — pruning selectively")

            
        # === Pre-Tier 1: Condense summary_of_events if nearing token limit ===
        if estimate_tokens(save_json) > 11800:
            if "summary_of_events" in campaign:
                campaign["summary_of_events"] = collapse_logs(campaign["summary_of_events"], keep_last=5)
                save_json = json.dumps(save_data, indent=2)


        # === Tier 1: Trim expandable logs ===
        if "summary_of_events" in campaign:
            events = campaign["summary_of_events"]
            if isinstance(events, list) and len(events) > 5:
                campaign["summary_of_events"] = events[-5:]

        if "session_notes" in campaign:
            campaign["session_notes"] = campaign["session_notes"][-3:]

        if "player_decisions" in campaign:
            campaign["player_decisions"] = campaign["player_decisions"][-5:]

        # === Tier 2: Prune notes from nested structures ===
        for npc in save_data.get("key_npcs", []):
            if isinstance(npc.get("interaction_notes"), list):
                npc["interaction_notes"] = npc["interaction_notes"][-3:]

        for faction in save_data.get("factions_encountered", []):
            if isinstance(faction.get("interaction_notes"), list):
                faction["interaction_notes"] = faction["interaction_notes"][-3:]

        for quest in campaign.get("active_quests", []):
            if isinstance(quest.get("key_decisions"), list):
                quest["key_decisions"] = quest["key_decisions"][-3:]

        # === Tier 3: Drop session summary ===
        save_json = json.dumps(save_data, indent=2)
        if estimate_tokens(save_json) > 12000:
            print("⚠️ Still over budget — removing session_summary")
            campaign["session_summary"] = None

            save_json = json.dumps(save_data, indent=2)

        # === Tier 3.5: Aggressively trim deceased NPCs and unused Known locations ===
        if estimate_tokens(save_json) > 12000:
            print("🗡️ Checking for deceased NPCs to prune")
            preserved_keys = {"relationship", "current_status", "name", "description"}
            death_phrases = ("deceased", "dead", "killed by", "killed during")

            for npc in save_data.get("key_npcs", []):
                status = (npc.get("relationship", {}).get("current_status") or "").lower()
                if any(phrase in status for phrase in death_phrases):
                    npc_keys = list(npc.keys())
                    for key in npc_keys:
                        if key not in preserved_keys:
                            npc.pop(key, None)

            save_json = json.dumps(save_data, indent=2)
            
            prune_known_locations_safe(
                save_data.get("known_locations", []),
                campaign,
                save_data.get("key_npcs", [])
            )



        # === Tier 4: Collapse older summaries ===
        if estimate_tokens(save_json) > 12000 and isinstance(campaign.get("summary_of_events"), list):
            collapsed = campaign["summary_of_events"][:-3]
            if collapsed:
                combined = "Previous events involved: " + "; ".join(e[:120] for e in collapsed) + "."
                campaign["summary_of_events"] = [combined] + campaign["summary_of_events"][-3:]

            save_json = json.dumps(save_data, indent=2)
            
            
            if estimate_tokens(save_json) > 12000:
                print("⚠️ Final token count still exceeds 8000 — continuing anyway. Sessions may be shorter.")




        # === Step 2: Summarize in chunks
        CHUNK_SIZE = 25000
        chunks = [full_transcript[i:i + CHUNK_SIZE] for i in range(0, len(full_transcript), CHUNK_SIZE)]

        chunk_prompt_template = """You are a Dungeons & Dragons campaign chronicler, entrusted with capturing the evolving tale of a solo adventurer across long and detailed sessions.

        Your task is to summarize a session log chunk with emotional accuracy and narrative continuity—while distilling it into the smallest space necessary to preserve the story’s core. This summary will later be used to reconstruct tone, character continuity, and plot progression.

        Your goals are:
        - Maintain immersion and emotional resonance.
        - Prioritize brevity without sacrificing critical nuance.
        - Optimize for token efficiency while keeping rehydration possible.

        Preserve:
        - Only the most pivotal emotional shifts, key choices, and dialogue that signal transformation.
        - Internal conflicts, evolving trust, and moments that redefine relationships or direction.
        - Important motivations, risks, or unfinished goals that will inform future play.

        Omit or reduce:
        - Procedural details (travel, combat, logistics) unless they change tone or trust.
        - Repetition, filler dialogue, and scenic description that doesn’t add new tension or clarity.
        - Dialogue that can be summarized narratively without losing meaning.

        Structure summaries to enable continuity between sessions:
        - Capture what’s emotionally unresolved.
        - Note any changes in character intent, belief, or tone.
        - Embed brief dialogue only when it anchors character voice or emotional tone.

        Write in third-person past tense. Prioritize momentum and insight over literal detail. When summarizing long chunks, favor evocative compression over exhaustive coverage.
        Transcript:
        {chunk}
        """

        chunk_summaries = []
        chunk_summary_tokens = 0

        for i, chunk in enumerate(chunks):
            prompt = chunk_prompt_template.format(chunk=chunk)
            try:
                response = gemini_model.generate_content(prompt)
                text = response.text.strip()
                chunk_summary_tokens += estimate_tokens(prompt) + estimate_tokens(text)
                chunk_summaries.append(text)
            except Exception as e:
                print(f"⚠️ Chunk {i} failed: {e}")
                chunk_summaries.append(f"(Chunk {i} failed)")

        # === Compress if needed
        MAX_CHUNK_TOKENS = 3000
        total_tokens = estimate_tokens("\n\n".join(chunk_summaries))
        if total_tokens > MAX_CHUNK_TOKENS:
            print("⚠️ Chunk summaries over token budget — generating unified session summary")
            try:
                full_summary_prompt = (
                    "You are a D&D chronicler. Merge the following chunk summaries into a single compact narrative that preserves tone, "
                    "key decisions, emotional beats, and character growth:\n\n" +
                    "\n\n".join(chunk_summaries)
                )
                final_summary_response = gemini_model.generate_content(full_summary_prompt)
                unified_summary = final_summary_response.text.strip()
                chunk_summaries = [unified_summary]
            except Exception as e:
                print(f"❌ Final summary compression failed: {e}")
                chunk_summaries = ["(Final compression failed)"]

        # === Update token state
        _, last_summarized_token_usage = load_history(thread_id)

        thread_path = os.path.join("data", f"{thread_id}.json")
        token_usage = 0
        if os.path.exists(thread_path):
            with open(thread_path, "r", encoding="utf-8") as f:
                thread_data = json.load(f)
                existing_token_usage = thread_data.get("token_usage", 0)
                summary_tokens_used = (
                    savefile_prompt_tokens +
                    savefile_response_tokens +
                    chunk_summary_tokens
                )
                token_usage = existing_token_usage + summary_tokens_used
                thread_data["last_summarized_token_usage"] = last_summarized_token_usage
            with open(thread_path, "w", encoding="utf-8") as f:
                json.dump(thread_data, f, indent=2)

        # === Final write
        payload = {
            "thread_id": thread_id,
            "summary_cache": {
                **save_data,
                "session_chunks": chunk_summaries
            },
            "timestamp": datetime.utcnow().isoformat(),
            "last_summarized_token_usage": last_summarized_token_usage,
            "token_usage": token_usage
        }
        
        # === Optional: perform in-memory merge to avoid destructive overwrite
        if os.path.exists(save_path):
            try:
                with open(save_path, "r", encoding="utf-8") as f:
                    existing_payload = json.load(f)

                existing_cache = existing_payload.get("summary_cache", {})
                new_cache = payload.get("summary_cache", {})

                for key in ["key_npcs", "factions_encountered", "known_locations"]:
                    if key in existing_cache and isinstance(existing_cache[key], list):
                        if key not in new_cache or not isinstance(new_cache[key], list):
                            new_cache[key] = existing_cache[key]
                        else:
                            existing_items = existing_cache[key]
                            new_items = new_cache[key]

                            # Extract names of already-present entries
                            new_names = {item.get("name") for item in new_items if isinstance(item, dict)}

                            # Append only items not already present by name
                            for item in existing_items:
                                if isinstance(item, dict) and item.get("name") not in new_names:
                                    new_items.append(item)

                            new_cache[key] = new_items


                # Update merged cache back into payload
                payload["summary_cache"] = new_cache

            except Exception as e:
                print(f"⚠️ Failed to merge with previous summary before write: {e}")


        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

        print(f"✅ Background summarization complete for thread: {thread_id}")

    except Exception:
        print("❌ Error in background summary task:")
        traceback.print_exc()
    finally:
        clear_summary_lock(thread_id)




async def build_summary_cache_from_thread(thread_id: str) -> str:
    """
    Fetches the full thread, chunks it, summarizes each chunk,
    and returns the full narrative to store in summary_cache.
    """
    raw_text = await get_flat_thread_messages(thread_id)
    chunks = chunk_text_by_tokens(raw_text, token_limit=25000)

    print(f"📚 {len(chunks)} chunks extracted from thread {thread_id}")

    summaries = []
    for i, chunk in enumerate(chunks):
        print(f"🧠 Summarizing chunk {i+1}/{len(chunks)}")
        summary = await summarize_chunk(chunk)
        summaries.append(f"CHUNK {i+1}:\n{summary.strip()}")

    full_summary = "\n\n---\n\n".join(summaries)
    print(f"✅ Full summary_cache generated with {len(summaries)} chunks")
    return full_summary




@app.get("/threads/sessions")
def list_all_sessions(api_key: str = Depends(verify_api_key)):
    store = list_threads()
    return [{"session_id": entry["session_id"], "thread_id": entry["thread_id"]} for entry in store]




@app.post("/api/save/from-thread")
async def save_from_thread(req: Request, api_key: str = Depends(verify_api_key)):
    data = await req.json()
    thread_id = data.get("thread_id")
    session_id = data.get("session_id") or str(uuid.uuid4())

    if not thread_id:
        raise HTTPException(status_code=400, detail="Missing thread_id")

    try:
        summary_cache = await build_summary_cache_from_thread(thread_id)

        save_file = SaveFile(
            session_id=session_id,
            timestamp=datetime.utcnow().isoformat(),
            summary_cache=summary_cache
        )

        save_path = os.path.join(SAVE_DIR, f"{session_id}.json")
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(save_file.model_dump(), f, indent=2)

        return {
            "message": "Summarized save created",
            "session_id": session_id
        }

    except Exception as e:
        logging.error(f"Failed to generate save from thread {thread_id}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Failed to generate save from thread")



client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
router = APIRouter()


from save_file_models import SaveFile

@app.get("/saves")
async def list_save_files(api_key: str = Depends(verify_api_key)):
    results = []
    for file in os.listdir("./saves"):
        if file.endswith(".json"):
            path = os.path.join("./saves", file)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    results.append({
                        "session_id": data.get("session_id"),
                        "timestamp": data.get("timestamp"),
                        "player_name": data.get("player_character", {}).get("name", "Unknown"),
                        "filename": file  # e.g., abc123_20250629T210745.json
                    })

                except Exception as e:
                    print(f"Failed to load {file}: {e}")
    return results


@save_router.post("/save/summarize-gemini")
async def summarize_with_gemini(
    request: Request, 
    background_tasks: BackgroundTasks, 
    api_key: str = Depends(verify_api_key)
):
    data = await request.json()
    thread_id = data.get("thread_id")
    if not thread_id:
        raise HTTPException(status_code=400, detail="Missing thread_id")

    gemini_model = request.app.state.gemini_model

    # Enqueue the background task
    background_tasks.add_task(summarize_in_background, gemini_model, thread_id)

    return {
        "status": "queued",
        "message": f"Summary for thread {thread_id} is being processed in background."
    }



@save_router.get("/save/{thread_id}")
async def get_save_file(thread_id: str, api_key: str = Depends(verify_api_key)):
    path = os.path.join("saves", f"{thread_id}.json")

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="SaveFile not found")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return JSONResponse(content=data)



class MergeRequest(BaseModel):
    old_id: str
    new_id: str

@app.post("/api/merge_saves")
async def merge_saves(req: MergeRequest, api_key: str = Depends(verify_api_key)):
    try:
        await asyncio.sleep(0.50)
        print(f"🔍 Merging: {req.old_id} → {req.new_id}")
        merge_save_files(req.old_id, req.new_id)
        return JSONResponse(content={"success": True, "merged_into": req.new_id})
    except FileNotFoundError as e:
        print(f"🚫 File missing: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        print(f"❌ Merge failed: {e}")
        raise HTTPException(status_code=500, detail=f"Merge failed: {str(e)}")




@save_router.get("/data/{thread_id}.json")
async def get_thread_data(thread_id: str, api_key: str = Depends(verify_api_key)):
    path = os.path.join("data", f"{thread_id}.json")

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Thread not found")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Return only the necessary fields for token tracking
    return JSONResponse(content={
        "token_usage": data.get("token_usage", 0),
        "last_summarized_token_usage": data.get("last_summarized_token_usage", 0)
    })



@router.get("/threads")
async def get_all_threads(api_key: str = Depends(verify_api_key)):
    return list_threads()



@app.get("/")
async def serve_index():
    return FileResponse("index.html")

@app.get("/script.js")
async def serve_script():
    return FileResponse("script.js")



@router.get("/thread/{thread_id}/token-usage")
async def get_thread_token_usage(thread_id: str, api_key: str = Depends(verify_api_key)):
    return get_token_usage(thread_id)



@app.get("/api/gemini/thread/{thread_id}/token-usage")
def get_gemini_token_usage(
    thread_id: str,
    api_key: str = Depends(verify_api_key)
):
    _, total = load_history(thread_id)
    return { "total": total }


@app.post("/api/tts")
async def proxy_tts(req: Request):
    try:
        data = await req.json()
        print("🔊 [TTS] Received request:", data)
        # Replace this with actual TTS call later
        return {"message": "TTS received"}
    except Exception as e:
        logging.error("TTS Proxy Error")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))



def get_thread_id_by_session(session_id: str) -> Optional[str]:
    try:
        filepath = "thread_store.json"
        if not os.path.exists(filepath):
            return None

        with open(filepath, "r", encoding="utf-8") as f:
            threads = json.load(f)

        for entry in threads:
            if entry.get("session_id") == session_id:
                return entry.get("thread_id")

        return None
    except Exception:
        return None





@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(router, prefix="/api/openai")
app.include_router(save_router, prefix="/api")
