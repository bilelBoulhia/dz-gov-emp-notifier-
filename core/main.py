import json
import requests
from pathlib import Path

from constants import (
    master,
    master_json,
    license,
    license_json,
)

from core.offer import fetch_offers
from helpers.api import send
from helpers.file import load_ids,save_ids,add


def main():
    sent_ids = load_ids()

    configs = [
        (license, license_json),
        (master, master_json),
    ]

    for niv_etude, json_file in configs:


        offers = fetch_offers(niv_etude=niv_etude)


        for offer in offers:
            add(offer, json_file)


        path = Path(json_file)
        if not path.exists():
            continue

        with open(path) as f:
            data = json.load(f)

        for post in data:
            post_id = post.get("id")
            if not post_id:
                continue

            if post_id in sent_ids:
                continue

            try:
                send(post)
                sent_ids.add(post_id)
                print(f"Sent: {post_id}")
            except requests.RequestException:
                continue

    save_ids(sent_ids)


if __name__ == "__main__":
    main()