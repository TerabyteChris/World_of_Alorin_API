import os
import json
import re


def sanitize_email(email: str) -> str:
    return re.sub(r"[^a-zA-Z0-9\-_.]", "_", email)


def get_token_usage_path(session_id: str, user_id: str) -> str:
    return os.path.join("saves", sanitize_email(user_id), f"{session_id}_usage.json")


def add_token_usage(session_id: str, usage: dict, user_id: str):
    if not usage:
        return

    path = get_token_usage_path(session_id, user_id)

    existing = {
        "prompt": 0,
        "completion": 0,
        "total": 0
    }
    if os.path.exists(path):
        with open(path, "r") as f:
            existing = json.load(f)

    existing["prompt"] += usage.get("prompt_tokens", 0)
    existing["completion"] += usage.get("completion_tokens", 0)
    existing["total"] += usage.get("total_tokens", 0)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(existing, f, indent=2)


def get_token_usage(session_id: str, user_id: str) -> dict:
    path = get_token_usage_path(session_id, user_id)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {"prompt": 0, "completion": 0, "total": 0}
