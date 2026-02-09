from offer import fetch_offers
from constants import license, master, master_json, license_json
from utils import add

configs = [
    (license, license_json, "license"),
    (master, master_json, "master"),
]

for niv_etude, json_file, label in configs:
    for offer in fetch_offers(niv_etude=niv_etude):
        if add(offer, json_file):
            print(f"{label} offer added: {offer.get('مكان إيداع أو إرسال ملفات الترشح')}")
