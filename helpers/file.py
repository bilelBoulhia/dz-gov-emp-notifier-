import json
from pathlib import Path

from constants import cache_dir


CACHE_DIR = Path(cache_dir)
CACHE_DIR.mkdir(parents=True, exist_ok=True)

SENT_FILE = CACHE_DIR / "ids.json"


def load_ids():
    if not SENT_FILE.exists():
        return set()

    with open(SENT_FILE, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_ids(sent_ids):
    with open(SENT_FILE, "w", encoding="utf-8") as f:
        json.dump(list(sent_ids), f, indent=2)

def add(obj: dict, json_file: str):
    file_path = Path(json_file)

    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    existing_ids = {o.get("id") for o in data if "id" in o}


    if obj.get("id") in existing_ids:
        return False

    data.append(obj)


    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return True