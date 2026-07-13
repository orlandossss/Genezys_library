import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("Genezeys_token")


querystring = {"language":"FR"}

payload = ""
headers = {
    "Accept": "application/json",
    "Authorization": f'{token}',
    "Referer": "https://app.genezys.xyz/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Google Chrome\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}

url = "https://app.genezys.xyz/api-prod-marketplace-service/stats/rarity-sale-prices"

response = requests.get(url, data=payload, headers=headers, params=querystring)

response_json = response.json()

def average_prices():
    all_prices = response_json['data']['averagePrices']

    for type in all_prices:
        if type['rarity'] == 'Limited':
            limited_price = type['averagePrice']
        elif type['rarity'] == 'Epic':
            epic_price = type['averagePrice']
        elif type['rarity'] == 'Legendary':
            legendary_price = type['averagePrice']
        elif type['rarity'] == 'Rare':
            rare_price = type['averagePrice']

    return limited_price, rare_price,epic_price, legendary_price


