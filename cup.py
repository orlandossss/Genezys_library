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

url = "https://app.genezys.xyz/api-prod-fantasy-game-service/cups"

response = requests.get(url, data=payload, headers=headers, params=querystring)

response_json = response.json()



def get_available_cups_id():
    cups_id = []
    for cup in response_json['data']:
        cup_id = cup['id']
        cups_id.append(cup_id)
    return cups_id

def get_available_cups_info():
    cups_info = []
    for cup in response_json['data']:
        cup_id = cup['id']
        accepted_rarities = cup['constraints']['acceptedRarities']
        cup_info = {
            'id': cup_id,
            'accepted_rarities': accepted_rarities,
        }
        cups_info.append(cup_info)
    return cups_info