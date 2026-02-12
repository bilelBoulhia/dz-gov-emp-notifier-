import requests

from constants import telegram_url, channel_id
from helpers.formaters import format_post


def send(post: dict):
    text = format_post(post)
    resp = requests.post(
        telegram_url,
        json={"chat_id": channel_id, "text": text, "parse_mode": "Markdown"},
        timeout=15
    )
    resp.raise_for_status()