import json

from offer import fetch_offers

from constants import (
    license,
    master,
    master_json,
    license_json
)


licence_offers = fetch_offers(niv_etude=license)
master_offers  = fetch_offers(niv_etude=master)
with open(license_json, "w", encoding="utf-8") as f:
    json.dump(master_offers, f, ensure_ascii=False, indent=2)
with open(master_json, "w", encoding="utf-8") as f:
    json.dump(licence_offers, f, ensure_ascii=False, indent=2)


