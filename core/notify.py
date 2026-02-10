from constants import (
 telegram_url,
channel_id
)
import requests


def send(text):
    url = telegram_url
    payload = {
        "chat_id": channel_id,
        "text": text
    }
    requests.post(url, json=payload, timeout=15)