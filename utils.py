import json
from pathlib import Path

def formater(offer: dict) -> str:
    lines = []
    for key, value in offer.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)



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
