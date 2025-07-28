# thread_registry.py
import os
import json
import uuid

REGISTRY_PATH = os.path.join("data", "gemini_sessions.json")

def _load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    return {}

def _save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

def get_or_create_thread_id_by_session(session_name):
    registry = _load_registry()

    if session_name in registry:
        return registry[session_name]

    thread_id = str(uuid.uuid4())
    registry[session_name] = thread_id
    _save_registry(registry)
    return thread_id
