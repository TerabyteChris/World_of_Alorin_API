import os
import json
import re
from storage import get_user_session_path 


def sanitize_email(email: str) -> str:
    return re.sub(r"[^a-zA-Z0-9\-_.]", "_", email)


def get_token_usage_path(session_id: str, user_id: str, campaign_name: str) -> str:
    base = os.path.join("saves", sanitize_email(user_id), campaign_name, "sessions")
    return os.path.join(base, f"{session_id}.json")

def add_token_usage(session_id: str, usage: dict, user_id: str, campaign_name: str):
    if not usage:
        return

    path = get_user_session_path(session_id, user_id)
    if not path or not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing = data.get("token_usage", {})
    if not isinstance(existing, dict):
        existing = {}

    for key in ["prompt", "completion", "total"]:
        if key not in existing or not isinstance(existing[key], int):
            existing[key] = 0

    existing["prompt"] += usage.get("prompt_tokens", 0)
    existing["completion"] += usage.get("completion_tokens", 0)
    existing["total"] += usage.get("total_tokens", 0)

    data["token_usage"] = existing

    # ✅ Store session_state counters if available
    import streamlit as st
    if "tokens_since_summary" in st.session_state:
        data["tokens_since_summary"] = st.session_state.tokens_since_summary
    if "tokens_since_rollover" in st.session_state:
        data["tokens_since_rollover"] = st.session_state.tokens_since_rollover

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)



def get_token_usage(session_id: str, user_id: str, campaign_name: str) -> dict:
    path = get_user_session_path(session_id, user_id)
    if not path or not os.path.exists(path):
        return {"prompt": 0, "completion": 0, "total": 0}

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    token_usage = data.get("token_usage", {})
    if not isinstance(token_usage, dict):
        return {"prompt": 0, "completion": 0, "total": 0}

    return {
        "prompt": token_usage.get("prompt", 0),
        "completion": token_usage.get("completion", 0),
        "total": token_usage.get("total", 0)
    }




