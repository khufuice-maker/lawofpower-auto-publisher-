# lawofpower-auto-publisher-
Book pdf
import os
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = "@lawofpower40"

if not TOKEN:
    raise ValueError("BOT_TOKEN မတွေ့ပါ")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHANNEL,
    "text": "✅ Telegram Auto Publisher Bot အလုပ်လုပ်နေပါပြီ။"
}

response = requests.post(url, data=data)
print(response.json())
