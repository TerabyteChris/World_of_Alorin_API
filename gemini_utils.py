from storage import load_history
from fastapi import HTTPException
from typing import List
from prompt_loader import load_prompt


CHUNK_SIZE = 25000  # character-based chunk size

def chunk_transcript(transcript: str, max_chars: int = CHUNK_SIZE) -> List[str]:
    return [transcript[i:i + max_chars] for i in range(0, len(transcript), max_chars)]

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

    return sum(
        m.get("token_usage", 0)
        for m in history
        if m["role"] in ("assistant", "gemini")  # assistant is used in your chat.py
    )


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
            summary = response.candidates[0].content.parts[0].text.strip()

            summaries.append(f"📍 Summary Part {i + 1}:\n{summary}")

        full_summary = "\n\n".join(summaries)
        return full_summary

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
