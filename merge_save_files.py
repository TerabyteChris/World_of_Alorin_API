import json
import os
from pathlib import Path
from typing import List, Dict

MERGE_CLASSES = ["key_npcs", "factions_encountered", "known_locations"]


def merge_save_files(old_id: str, new_id: str) -> None:
    try:
        base_path = Path("saves")
        old_path = base_path / f"{old_id}.json"
        new_path = base_path / f"{new_id}.json"

        print(f"📂 Merging saves: {old_path} → {new_path}")

        if not old_path.exists():
            raise FileNotFoundError(f"Old file not found: {old_path}")
        if not new_path.exists():
            raise FileNotFoundError(f"New file not found: {new_path}")

        old_data = json.loads(old_path.read_text(encoding="utf-8"))
        new_data = json.loads(new_path.read_text(encoding="utf-8"))

        old_cache = old_data.get("summary_cache", {})
        new_cache = new_data.get("summary_cache", {})

        for key in MERGE_CLASSES:
            print(f"🔎 Checking class: {key}")
            if key in old_cache and isinstance(old_cache[key], list):
                if key not in new_cache or not isinstance(new_cache[key], list):
                    print(f"➕ Adding all {len(old_cache[key])} to new_cache[{key}]")
                    new_cache[key] = old_cache[key]
                else:
                    existing_items = old_cache[key]
                    new_items = new_cache[key]

                    new_names = {item.get("name") for item in new_items if isinstance(item, dict)}

                    additions = 0
                    for item in existing_items:
                        if isinstance(item, dict) and item.get("name") not in new_names:
                            new_items.append(item)
                            additions += 1

                    print(f"🔁 Merged {additions} missing items into new_cache[{key}]")

                    new_cache[key] = new_items


            else:
                print(f"⚠️ Skipped {key} — not found or not a list")

        new_data["summary_cache"] = new_cache

        print("💾 Writing merged file...")
        new_path.write_text(json.dumps(new_data, indent=2, ensure_ascii=False), encoding="utf-8")
        print("✅ Merge complete.")
        
    except Exception as e:
        print(f"❌ Error inside merge_save_files: {e}")
        raise  # Re-raise so the API handler catches and returns a 500

