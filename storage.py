# storage.py — Filesystem-based memory for Gemini threads

import os
import json
from save_file_models import SaveFile
import re
from typing import Tuple, List, Dict
from campaign_utils import get_user_base_path

BASE_DIR = "/opt/alorin_api/data"
os.makedirs(BASE_DIR, exist_ok=True)  # Ensure dir exists

def _get_path(thread_id: str) -> str:
    """Get full path to thread's JSON file."""
    return os.path.join(BASE_DIR, f"{thread_id}.json")

def sanitize_email(email: str) -> str:
    return re.sub(r"[^a-zA-Z0-9\-_.]", "_", email)

def get_user_session_path(session_id: str, user_id: str) -> str:
    user_base = os.path.join("saves", sanitize_email(user_id))
    if not os.path.exists(user_base):
        return None  # Avoid FileNotFoundError

    for campaign_name in os.listdir(user_base):
        session_path = os.path.join(user_base, campaign_name, "sessions", f"{session_id}.json")
        if os.path.exists(session_path):
            return session_path

    return None



def load_history(thread_id: str, user_id: str = None):
    path = get_user_session_path(thread_id, user_id)
    if not path or not os.path.exists(path):
        return [], 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Failed to load or parse thread history for {thread_id}: {e}")
        return [], 0

    raw_messages = data.get("messages", [])
    if not isinstance(raw_messages, list):
        print(f"⚠️ Malformed message list in thread {thread_id}")
        return [], 0

    messages = [m for m in raw_messages if isinstance(m, dict) and "role" in m and "content" in m]
    total_tokens = data.get("token_usage", 0)
    if not isinstance(total_tokens, int):
        total_tokens = total_tokens.get("total", 0) if isinstance(total_tokens, dict) else 0

    return messages, total_tokens





def save_message(session_id, role, content, token_usage=None, user_id=None):
    path = get_user_session_path(session_id, user_id)
    data = {}

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

    # Ensure 'messages' key exists and is a list
    if "messages" not in data:
        data["messages"] = []

    data["messages"].append({
        "role": role,
        "content": content,
        "token_usage": token_usage
    })

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)




def update_last_summarized_token_usage(session_id: str, user_id: str, value: int):
    path = get_user_session_path(session_id, user_id)
    if not path or not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["last_summarized_token_usage"] = value
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)



def load_full_save(session_id: str, user_id: str) -> List[Dict]:
    path = get_user_session_path(session_id, user_id)
    if not path or not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


    
def get_all_thread_ids() -> list[str]:
    data_dir = "data"
    if not os.path.exists(data_dir):
        return []
    return [
        filename.replace(".json", "")
        for filename in os.listdir(data_dir)
        if filename.endswith(".json")
    ]

def load_token_usage(session_id: str, user_id: str) -> dict:
    """Return a dict of token usage for a session."""
    path = get_user_session_path(session_id, user_id)
    if not path or not os.path.exists(path):
        return {"prompt": 0, "completion": 0, "total": 0}
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        usage = data.get("token_usage", {})
        return {
            "prompt": usage.get("prompt_tokens", 0),
            "completion": usage.get("completion_tokens", 0),
            "total": usage.get("total_tokens", 0)
        }

        
def load_summary_cache(session_id: str, user_id: str) -> dict:
    base_path = get_user_base_path(user_id)
    for campaign_name in os.listdir(base_path):
        sessions_dir = os.path.join(base_path, campaign_name, "sessions")
        if not os.path.exists(sessions_dir):
            continue
        session_path = os.path.join(sessions_dir, f"{session_id}.json")
        if os.path.exists(session_path):
            with open(session_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("summary_cache", {})
    return {}
