import requests
import hashlib
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from constants import (
    URL,
    HEADERS,
    date_name,
    locatisation,
    day_limit,

)

class JobOffer:
    def __init__(self, title):
        self.title = title
        self.sent = False
        self.fields = {}

    def set(self, key, value):
        self.fields[self._clean(key)] = self._clean(value)

    def get(self, key, default=None):
        return self.fields.get(key, default)

    def _clean(self, text):
        if not text:
            return ""
        return " ".join(text.split())

    def _id(self):
        date_val = self.fields.get(date_name)
        place = self.fields.get("مكان إيداع أو إرسال ملفات الترشح")

        if not date_val or not place:
            return None

        raw = f"{date_val}|{self.title}|{place}"
        raw = self._clean(raw)

        return hashlib.sha256(raw.encode("utf-8")).hexdigest()

    def to_dict(self):
        return {
            "id": self._id(),
            "title": self.title,
            "sent": self.sent,
            **self.fields
        }

    def __str__(self):
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)





def fetch_offers(niv_etude, localisation=locatisation, days_limit=day_limit):
        payload = {
            "NivEtude": str(niv_etude),
            "precisions": "",
            "organisatrice": "99",
            "localisation": localisation,
            "mode_rec": "99",
            "grade888": "9999",
            "tri": "g"
        }

        response = requests.post(URL, data=payload, headers=HEADERS, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        offers = []
        current_offer = None

        for tr in soup.find_all("tr"):
            ths = tr.find_all("th")
            tds = tr.find_all("td")

            if len(ths) == 1 and ths[0].get("colspan"):
                title = ths[0].get_text(strip=True)
                current_offer = JobOffer(title)
                offers.append(current_offer)
                continue

            if len(tds) == 2 and current_offer:
                key = tds[0].get_text(strip=True)
                value = tds[1].get_text(strip=True)
                if key:
                    current_offer.set(key, value)

        available_offers = []
        cutoff_date = datetime.today().date() - timedelta(days=days_limit)

        for offer in offers:
            date_str = offer.get(date_name)
            if not date_str:
                continue
            try:
                offer_date = datetime.strptime(date_str, "%d/%m/%Y").date()
            except ValueError:
                continue

            if offer_date >= cutoff_date:
                available_offers.append(offer.to_dict())

        return available_offers

