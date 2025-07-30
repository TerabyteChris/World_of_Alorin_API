# campaign_utils.py

import os
import json
import re
from datetime import datetime
from typing import List, Dict


def sanitize_email(email: str) -> str:
    return re.sub(r"[^a-zA-Z0-9\-_.]", "_", email)


def get_user_base_path(user_email: str) -> str:
    return os.path.join("saves", sanitize_email(user_email))


def get_campaigns_path(user_email: str) -> str:
    return os.path.join(get_user_base_path(user_email), "campaigns.json")


def list_campaigns(user_email: str) -> List[Dict]:
    """Returns a list of all campaigns (from folders) under this user's directory."""
    campaigns = []
    base = get_user_base_path(user_email)
    if not os.path.exists(base):
        return []

    for entry in os.listdir(base):
        campaign_path = os.path.join(base, entry, "campaign.json")
        if os.path.exists(campaign_path):
            with open(campaign_path, "r", encoding="utf-8") as f:
                try:
                    campaigns.append(json.load(f))
                except json.JSONDecodeError:
                    continue
    return campaigns



def create_campaign(user_email: str, name: str) -> Dict:
    campaign_id = name.strip()
    user_path = get_user_base_path(user_email)
    campaign_folder = os.path.join(user_path, name.strip())  # Use clean campaign name, not slugified ID
    os.makedirs(os.path.join(campaign_folder, "sessions"), exist_ok=True)

    metadata = {
        "id": campaign_id,
        "name": name,
        "created_at": datetime.now().isoformat()
    }

    # Save individual campaign metadata
    with open(os.path.join(campaign_folder, "campaign.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    # Update campaigns index
    campaigns = list_campaigns(user_email)
    campaigns.append(metadata)

    create_session(user_email, campaign_id)
    return metadata



def list_sessions(user_email: str, campaign_id: str) -> List[str]:
    session_folder = os.path.join(get_user_base_path(user_email), campaign_id, "sessions")
    if not os.path.exists(session_folder):
        return []
    return sorted([
        f.replace(".json", "")
        for f in os.listdir(session_folder)
        if f.endswith(".json")
    ])


def create_session(user_email: str, campaign_id: str) -> str:
    # Determine session directory
    session_dir = os.path.join(get_user_base_path(user_email), campaign_id, "sessions")
    os.makedirs(session_dir, exist_ok=True)

    # Count existing sessions
    existing_files = [f for f in os.listdir(session_dir) if f.endswith(".json")]
    session_number = len(existing_files)

    # Build session ID
    now = datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H-%M")
    session_id = f"Session {session_number} {timestamp_str}"

    # Path to save
    session_path = os.path.join(session_dir, f"{session_id}.json")

    # Create empty session data
    data = {
        "thread_id": session_id,
        "timestamp": now.isoformat(),
        "messages": [],
        "token_usage": 0,
        "summary_chunks": [],
        "last_summarized_token_usage": 0,
        "startup_injected": False,
    }

    # Save to disk
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return session_id


def readable_session_names(sessions: List[str]) -> List[str]:
    result = []
    for s in sessions:
        try:
            parts = s.split("_")
            idx = parts[1]
            dt = datetime.strptime(parts[2], "%Y-%m-%dT%H-%M-%S")
            readable = f"Session {idx} - {dt.strftime('%b %d, %Y %I:%M %p')}"
        except Exception:
            readable = s
        result.append(readable)
    return result


def extract_session_id(readable_name: str) -> str:
    # Pass-through if already a valid filename
    if readable_name.endswith(".json"):
        return readable_name.replace(".json", "")
    return readable_name  # readable_name is the full session ID like "Session 0 2025-07-30 14-18"

