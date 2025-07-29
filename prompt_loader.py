import os

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "prompts")

def load_prompt(name: str) -> str:
    path = os.path.join(PROMPT_DIR, f"{name}.txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()