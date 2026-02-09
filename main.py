from offer import fetch_offers
from constants import license, master, master_json, license_json
from utils import add


for offer in fetch_offers(niv_etude=license):
    if add(offer, license_json):
        print(f"icense offer added: {offer.get('مكان إيداع أو إرسال ملفات الترشح')}")


for offer in fetch_offers(niv_etude=master):
    if add(offer, master_json):
        print(f"master offer added: {offer.get('مكان إيداع أو إرسال ملفات الترشح')}")


