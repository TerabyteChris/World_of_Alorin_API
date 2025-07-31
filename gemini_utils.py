from storage import load_history, get_user_session_path
from fastapi import HTTPException
from typing import List
from prompt_loader import load_prompt
from pathlib import Path
import os, traceback, time, json, re
from datetime import datetime
from save_helpers import get_save_file_path
from save_file_models import SaveFile
from token_tracker import get_token_usage

CHUNK_SIZE = 25000  # character-based chunk size
COOLDOWN_SECONDS = 180  # Customize: how long to wait before allowing another run

def chunk_transcript(transcript: str, max_chars: int = CHUNK_SIZE) -> List[str]:
    return [transcript[i:i + max_chars] for i in range(0, len(transcript), max_chars)]

def get_total_tokens(thread_id: str, user_email, current_tokens: int = 0, ) -> int:
    """
    Returns the total tokens used in a thread, including saved history and optional current count.
    
    Parameters:
    - thread_id (str): The thread/session ID
    - current_tokens (int): Tokens used in the current request (default: 0)
    
    Returns:
    - int: Cumulative token usage for the thread
    """
    try:
        history, _ = load_history(thread_id, user_email)
    except Exception:
        history = []

    return sum(
        m.get("token_usage", 0)
        for m in history
        if m["role"] in ("assistant", "gemini")  # assistant is used in your chat.py
    )


def summarize_chat_history_with_gemini(gemini_model, user_email, campaign_name, thread_id: str) -> str:
    try:
        # === Load chat history (assumes load_history returns list of { role, content })
        messages, _ = load_history(thread_id, user_email)
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

            text = ""
            try:
                text = (
                    response.candidates[0].content.parts[0].text.strip()
                    if response and response.candidates and response.candidates[0].content.parts
                    else ""
                )
            except Exception as inner_e:
                print("⚠️ Failed to extract summary text:", inner_e)

            summaries.append(f"📍 Summary Part {i + 1}:\n{text or '[Empty summary]'}")

        full_summary = "\n\n".join(summaries)

        # === Save summaries to session file ===
        path = get_user_session_path(thread_id, user_email)
        if not path or not os.path.exists(path):
            raise FileNotFoundError(f"Session file not found at: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["summary_chunks"] = summaries
        token_usage = get_token_usage(thread_id, user_email, campaign_name)
        data["last_summarized_token_usage"] = get_total_tokens(thread_id, user_email, 0)
        data["startup_injected"] = True
        data["tokens_since_summary"] = 0

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return full_summary.strip()

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Gemini summarization failed.")



def get_gemini_input(session_context: str, is_new_campaign=False) -> str:
    if is_new_campaign:
        return load_prompt("new_campaign_prompt") + "\n\n" + session_context
    elif session_context.strip() == "":
        return load_prompt("startup_script")
    else:
        return load_prompt("continuation_prompt") + "\n\n" + session_context
    
def build_final_prompt(main_prompt: str) -> str:
    return load_prompt("static_instructions") + "\n\n" + main_prompt

def safe_parse_json(raw_text: str):
    # Remove triple backticks or language hints like ```json
    clean = re.sub(r"```(?:json)?", "", raw_text.strip(), flags=re.IGNORECASE)
    try:
        return json.loads(clean)
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON: {e}")
        return {}

def estimate_tokens(text: str) -> int:
    # Rough heuristic: 1 token ≈ 4 characters
    return len(text) // 4

def collapse_logs(logs: list[str], keep_last: int = 3) -> list[str]:
    if not isinstance(logs, list) or len(logs) <= keep_last + 1:
        return logs

    combined_text = "; ".join(log[:120].strip() for log in logs[:-keep_last])
    merged = f"Earlier sessions involved: {combined_text}."
    return [merged] + logs[-keep_last:]

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
    for quest in campaign.get("active_quests") or []:
        desc = norm(quest.get("description") or "")
        for loc in locations or []:
            loc_name = norm(loc.get("name"))
            if loc_name and loc_name in desc:
                used_locations.add(loc_name)

    # 3. From NPC presence
    npc_names = {norm(npc.get("name")) for npc in (npcs or []) if isinstance(npc, dict)}
    for loc in locations or []:
        loc_name = norm(loc.get("name"))
        for npc_name in (loc.get("npcs_present") or []):
            if norm(npc_name) in npc_names:
                used_locations.add(loc_name)

    # 4. Prune unused locations
    for loc in locations or []:
        loc_name = norm(loc.get("name"))
        if loc_name not in used_locations:
            for key in list(loc.keys()):
                if key not in ("name", "history"):
                    loc[key] = None

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

def summarize_in_background(gemini_model, thread_id, user_email, campaign_name):
    if is_summary_locked(thread_id):
        print(f"⚠️ Summary already running or recently finished for thread {thread_id}. Skipping.")
        return

    set_summary_lock(thread_id)

    try:
        print(f"🧠 Starting background summarization for thread: {thread_id}")

        # === Load chat history
        messages, _ = load_history(thread_id, user_email)
        if not messages:
            print(f"❌ No messages to summarize for thread {thread_id}")
            return

        # === Flatten full transcript
        full_transcript = "\n\n".join(f"{m['role'].capitalize()}: {m['content']}" for m in messages)

        # === Load previous SaveFile (if exists)
        previous_summary = None
        save_path = get_save_file_path(user_email, campaign_name)

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
        print("DEBUG user_email:", repr(user_email))
        _, last_summarized_token_usage = load_history(thread_id, user_email)

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
        def normalize_npc(npc: dict) -> dict:
            npc.setdefault("name", "Unnamed")
            npc.setdefault("description", "")
            npc.setdefault("goals", "")
            npc.setdefault("interaction_notes", [])
            npc.setdefault("relationship", {})
            return npc

        def normalize_faction(faction: dict) -> dict:
            faction.setdefault("name", "Unnamed Faction")
            faction.setdefault("goals", "")
            faction.setdefault("interaction_notes", [])
            faction.setdefault("interaction_summary", "")
            faction.setdefault("times_encountered", 0)
            return faction

        def normalize_location(loc: dict) -> dict:
            loc.setdefault("name", "Unnamed Location")
            loc.setdefault("description", "")
            loc.setdefault("key_features", [])
            loc.setdefault("npcs_present", [])
            loc.setdefault("factions_present", [])
            loc.setdefault("history", "")
            return loc

        # Inject session_chunks into summary_cache
        summary_cache = {
            **save_data,
            "session_chunks": chunk_summaries
        }

        summary_cache["key_npcs"] = [normalize_npc(n) for n in summary_cache.get("key_npcs", [])]
        summary_cache["factions_encountered"] = [normalize_faction(f) for f in summary_cache.get("factions_encountered", [])]
        summary_cache["known_locations"] = [normalize_location(l) for l in summary_cache.get("known_locations", [])]

        # Create validated payload
        # Normalize + inject required fields before validation
        summary_cache = {
            **save_data,
            "session_chunks": chunk_summaries
        }

        summary_cache["key_npcs"] = [normalize_npc(n) for n in summary_cache.get("key_npcs", [])]
        summary_cache["factions_encountered"] = [normalize_faction(f) for f in summary_cache.get("factions_encountered", [])]
        summary_cache["known_locations"] = [normalize_location(l) for l in summary_cache.get("known_locations", [])]

        # Fallbacks for required root-level fields
        session_id = thread_id  # or derive it separately if needed
        player_character = summary_cache.get("player_character") or {
            "name": "Unnamed Hero",
            "race": "Unknown",
            "character_class": "Unknown",
            "level": 1,
            "background": "",
            "alignment": "Neutral",
            "features": [],
            "skills": [],
            "inventory": [],
            "currency": {}
        }

        # Final validated payload
        payload = SaveFile.model_validate({
            "thread_id": thread_id,
            "session_id": session_id,
            "summary_cache": summary_cache,
            "timestamp": datetime.utcnow().isoformat(),
            "last_summarized_token_usage": last_summarized_token_usage,
            "token_usage": token_usage,
            "startup_injected": True,
            "player_character": player_character
        }).model_dump(mode="json", exclude_none=True)

        
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