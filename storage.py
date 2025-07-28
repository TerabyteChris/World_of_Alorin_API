# storage.py — Filesystem-based memory for Gemini threads

import os
import json

BASE_DIR = "/opt/alorin_api/data"
os.makedirs(BASE_DIR, exist_ok=True)  # Ensure dir exists

def _get_path(thread_id: str) -> str:
    """Get full path to thread's JSON file."""
    return os.path.join(BASE_DIR, f"{thread_id}.json")

def load_history(thread_id):
    path = os.path.join("data", f"{thread_id}.json")
    
    if not os.path.exists(path):
        return [], 0

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"⚠️ Failed to load or parse thread history for {thread_id}: {e}")
        return [], 0

    # Ensure messages is a list
    raw_messages = data.get("messages", [])
    if not isinstance(raw_messages, list):
        print(f"⚠️ Malformed message list in thread {thread_id}")
        return [], 0

    # Filter out invalid message entries
    messages = []
    for m in raw_messages:
        if isinstance(m, dict) and "role" in m and "content" in m:
            messages.append(m)
        else:
            print(f"⚠️ Skipped malformed message in {thread_id}: {m}")

    # Total token count (int or fallback to 0)
    total_tokens = data.get("token_usage", 0)
    if not isinstance(total_tokens, int):
        total_tokens = 0

    return messages, total_tokens




def save_message(thread_id, role, content, token_usage=None):
    path = os.path.join("data", f"{thread_id}.json")

    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
    else:
        data = {
            "thread_id": thread_id,
            "messages": [],
            "token_usage": 0,
            "last_summarized_token_usage": 0  # <-- add default if missing
        }

    message = { "role": role, "content": content }
    if token_usage is not None:
        message["token_usage"] = token_usage
        data["token_usage"] += token_usage

    data["messages"].append(message)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def update_last_summarized_token_usage(thread_id, value: int):
    path = os.path.join("data", f"{thread_id}.json")
    if not os.path.exists(path):
        return
    with open(path, "r") as f:
        data = json.load(f)
    data["last_summarized_token_usage"] = value
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


