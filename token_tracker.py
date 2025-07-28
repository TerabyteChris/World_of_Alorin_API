import os
import json

# === Path to persistent store ===
TOKEN_TRACK_FILE = "./thread_token_usage.json"

# === Load usage database ===
if os.path.exists(TOKEN_TRACK_FILE):
    with open(TOKEN_TRACK_FILE, "r") as f:
        token_usage_db = json.load(f)
else:
    token_usage_db = {}

# === Add token usage to a thread ===
def add_token_usage(thread_id: str, usage: dict):
    if not usage:
        return

    existing = token_usage_db.get(thread_id, {"prompt": 0, "completion": 0, "total": 0})
    existing["prompt"] += usage.get("prompt_tokens", 0)
    existing["completion"] += usage.get("completion_tokens", 0)
    existing["total"] += usage.get("total_tokens", 0)

    token_usage_db[thread_id] = existing

    with open(TOKEN_TRACK_FILE, "w") as f:
        json.dump(token_usage_db, f, indent=2)

# === Retrieve usage for a thread ===
def get_token_usage(thread_id: str) -> dict:
    return token_usage_db.get(thread_id, {"prompt": 0, "completion": 0, "total": 0})
