from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Union, Any
from datetime import datetime


# === Universal Coercion Utilities ===

def coerce_to_str(v: Any) -> Optional[str]:
    if v is None or v == "":
        return None
    return str(v)

def coerce_to_int(v: Any) -> Optional[int]:
    try:
        return int(v)
    except (TypeError, ValueError):
        return None

def coerce_to_float(v: Any) -> Optional[float]:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None

def coerce_to_str_list(v: Union[str, List[str], None]) -> List[str]:
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        return v
    return []

def coerce_to_dict(v: Any) -> Dict:
    if isinstance(v, dict):
        return v
    return {}

def coerce_to_model_list(v: Union[dict, List[dict], None]) -> List[dict]:
    if isinstance(v, dict):
        return [v]
    if isinstance(v, list):
        return v
    return []


# === Models ===

class Relationship(BaseModel):
    history: Optional[str]
    current_status: Optional[str]
    trust_level: Optional[int]


class KeyNPC(BaseModel):
    name: str
    description: Optional[str]
    role: Optional[str]
    known_alliances: Optional[str]
    known_enemies: Optional[str]
    motives_or_secrets: Optional[str]
    relationship: Optional[Relationship]
    times_met: Optional[int]
    interaction_notes: Optional[List[str]]
    goals: Optional[str]

    _normalize_interaction_notes = validator("interaction_notes", pre=True, allow_reuse=True)(coerce_to_str_list)
    _normalize_goals = validator("goals", pre=True, allow_reuse=True)(coerce_to_str)
    _normalize_times_met = validator("times_met", pre=True, allow_reuse=True)(coerce_to_int)

class Faction(BaseModel):
    name: str
    goals: Optional[str]
    interaction_summary: Optional[str]
    times_encountered: Optional[int]
    interaction_notes: Optional[List[str]]
    
    _normalize_times_encountered = validator("times_encountered", pre=True, allow_reuse=True)(coerce_to_int)
    _normalize_interaction_notes = validator("interaction_notes", pre=True, allow_reuse=True)(coerce_to_str_list)


class ActiveQuest(BaseModel):
    title: str
    description: str
    status: str
    key_decisions: Optional[List[str]]

    _normalize_key_decisions = validator("key_decisions", pre=True, allow_reuse=True)(coerce_to_str_list)
    
    
class Location(BaseModel):
    name: str
    description: Optional[str]
    key_features: Optional[List[str]]
    npcs_present: Optional[List[str]]
    factions_present: Optional[List[str]]
    history: Optional[str]

    _normalize_key_features = validator("key_features", pre=True, allow_reuse=True)(coerce_to_str_list)
    _normalize_npcs_present = validator("npcs_present", pre=True, allow_reuse=True)(coerce_to_str_list)
    _normalize_factions_present = validator("factions_present", pre=True, allow_reuse=True)(coerce_to_str_list)



class CampaignState(BaseModel):
    summary_of_events: Optional[List[str]]
    world_state: Optional[str]
    world_modifiers: Optional[List[str]]
    session_notes: Optional[List[str]]
    player_decisions: Optional[List[str]]
    ongoing_objectives: Optional[List[str]]
    inventory_and_equipment: Optional[List[str]]
    campaign_variables: Optional[List[str]]
    current_location: Optional[str]
    current_situation: Optional[str]
    active_quests: Optional[List[ActiveQuest]]



class PlayerCharacter(BaseModel):
    name: str
    character_class: str
    race: str
    background: str
    level: int

    alignment: Optional[str] = None
    max_hp: Optional[int] = None
    current_hp: Optional[int] = None
    initiative: Optional[int] = None
    armor_class: Optional[int] = None
    speed: Optional[int] = None
    hit_dice: Optional[str] = None
    death_saves: Optional[str] = None

    ability_scores: Optional[Dict[str, Dict[str, int]]] = None
    saving_throws: Optional[List[str]] = None
    skills: Optional[List[str]] = None
    passive_perception: Optional[int] = None

    spell_slots: Optional[Dict[str, int]] = None
    spells: Optional[List[str]] = None

    attacks_and_spellcasting: Optional[str] = None
    inventory: Optional[List[str]] = None
    currency: Optional[Dict[str, int]] = None

    traits: Optional[str] = None
    ideals: Optional[str] = None
    bonds: Optional[str] = None
    flaws: Optional[str] = None
    features: Optional[str] = None
    appearance: Optional[str] = None
    backstory: Optional[str] = None

    notable_traits: Optional[str] = None

    # === Validators ===
    _normalize_strs = validator(
        "name", "character_class", "race", "background", "alignment",
        "notable_traits", "attacks_and_spellcasting", "traits", "ideals",
        "bonds", "flaws", "features", "appearance", "backstory", "hit_dice", "death_saves",
        pre=True, allow_reuse=True
    )(coerce_to_str)

    _normalize_ints = validator(
        "level", "max_hp", "current_hp", "initiative", "armor_class",
        "speed", "passive_perception",
        pre=True, allow_reuse=True
    )(coerce_to_int)

    _normalize_inventory = validator("inventory", "skills", "saving_throws", "spells", pre=True, allow_reuse=True)(coerce_to_str_list)
    _normalize_spell_slots = validator("spell_slots", "currency", pre=True, allow_reuse=True)(coerce_to_dict)
    _normalize_ability_scores = validator("ability_scores", pre=True, allow_reuse=True)(coerce_to_dict)




class SaveFile(BaseModel):
    session_id: str
    timestamp: datetime
    player_character: PlayerCharacter
    key_npcs: Optional[List[KeyNPC]] = None
    known_locations: Optional[List[Location]] = None
    factions_encountered: Optional[List[Faction]] = None
    campaign: Optional[CampaignState] = None
    session_chunks: Optional[List[str]] = None  # Optional session summaries

    # === Validators ===
    _normalize_session_id = validator("session_id", pre=True, allow_reuse=True)(coerce_to_str)
    _normalize_timestamp = validator("timestamp", pre=True, allow_reuse=True)(lambda v: datetime.fromisoformat(v) if isinstance(v, str) else v)