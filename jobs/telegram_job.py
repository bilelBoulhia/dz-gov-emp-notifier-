import json
from pathlib import Path
import requests
from core.utils import send
from constants import license_json, master_json

for file_path in [license_json, master_json]:
    path = Path(file_path)
    if not path.exists():
        continue

    with open(path) as f:
        data = json.load(f)

    for post in data:
        if post.get("sent"):
            continue

        try:
            send(post)
        except requests.RequestException as e:
            continue

        post["sent"] = True


    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
