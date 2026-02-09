import os
import tempfile

URL = "http://www.concours-fonction-publique.gov.dz/ar/Liste.asp"



HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}
date_name = "تـاريخ الإدراج في الموقــع"

locatisation=16

day_limit=15

license=4
master=2

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
channel_id = os.getenv("TELEGRAM_CHANNEL_ID")
telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
tmp_dir = tempfile.gettempdir()

license_json = os.path.join(tmp_dir, "license.json")
master_json  = os.path.join(tmp_dir, "master.json")
