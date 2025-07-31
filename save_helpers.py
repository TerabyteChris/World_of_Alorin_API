import os, json
from save_file_models import SaveFile
from campaign_utils import get_campaign_path

SAVE_FILENAME = "save.json"

def get_save_file_path(user_email: str, campaign_name: str) -> str:
    return os.path.join(get_campaign_path(user_email, campaign_name), SAVE_FILENAME)


# === Normalization Helpers ===

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
    faction.setdefault("interaction_summary", "")
    faction.setdefault("interaction_notes", [])
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

def normalize_summary_cache(summary_cache: dict) -> dict:
    summary_cache["key_npcs"] = [normalize_npc(n) for n in summary_cache.get("key_npcs", [])]
    summary_cache["factions_encountered"] = [normalize_faction(f) for f in summary_cache.get("factions_encountered", [])]
    summary_cache["known_locations"] = [normalize_location(l) for l in summary_cache.get("known_locations", [])]
    return summary_cache


# === File Operations ===

def write_save_file(user_id: str, campaign_name: str, summary_cache: dict) -> str:
    """Creates or overwrites the save file for a campaign."""
    path = get_save_file_path(user_id, campaign_name)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    validated = SaveFile.model_validate({
        "thread_id": f"{user_id}_{campaign_name}",
        "summary_cache": normalize_summary_cache(summary_cache)
    })

    with open(path, "w", encoding="utf-8") as f:
        f.write(validated.model_dump_json(indent=2))
    return path


def read_save_file(user_id: str, campaign_name: str) -> SaveFile:
    """Reads the current save file for a campaign."""
    path = get_save_file_path(user_id, campaign_name)
    with open(path, "r", encoding="utf-8") as f:
        return SaveFile.model_validate_json(f.read())


def update_save_file(user_id: str, campaign_name: str, patch: dict) -> str:
    """Updates fields inside the campaign save file."""
    save = read_save_file(user_id, campaign_name)
    for key, value in patch.items():
        if hasattr(save.summary_cache, key):
            setattr(save.summary_cache, key, value)
    return write_save_file(user_id, campaign_name, save.summary_cache.model_dump())


def save_file_to_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    model = SaveFile(**raw)

    chunks = []

    if model.player_character:
        chunks.append(f"Character: {model.player_character.name} the {model.player_character.race} {model.player_character.character_class}")

    if model.key_npcs:
        for npc in model.key_npcs:
            chunks.append(f"NPC: {npc.name} ({npc.role}) — {npc.description}")

    if model.factions_encountered:
        for fac in model.factions_encountered:
            chunks.append(f"Faction: {fac.name} — {fac.goals}")

    if model.campaign and model.campaign.summary_of_events:
        chunks.append("Recent events:")
        chunks.extend(model.campaign.summary_of_events[-3:])

    if model.session_chunks:
        chunks.append("Recent session summary:")
        chunks.extend(model.session_chunks[-2:])

    return "\n\n".join(chunks)
