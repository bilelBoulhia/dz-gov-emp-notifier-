import json
from pathlib import Path

import requests

from constants import telegram_url, channel_id


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

def format_post_for_telegram(post: dict) -> str:
    lines = []

    # title
    title = post.get("title", "")
    if title:
        lines.append(f"📌 {title}\n")

    for key, value in post.items():
        if key in ["title", "sent", "id"]:
            continue
        if value:

            value_str = str(value)
            lines.append(f"*{key}*: {value_str}")

    return "\n".join(lines)


def send(post: dict):
    text = format_post_for_telegram(post)  # get readable string
    resp = requests.post(
        telegram_url,
        json={"chat_id": channel_id, "text": text, "parse_mode": "Markdown"},
        timeout=15
    )
    resp.raise_for_status()


