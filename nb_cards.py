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

url = "https://app.genezys.xyz/api-prod-collection-service/cards/user-card-summary"

response = requests.get(url, data=payload, headers=headers, params=querystring)

response_json = response.json()

def nb_common_cards():
    common_cards = response_json['data']['linked_common_nb']
    return common_cards

def nb_limited_cards():
    limited_cards = response_json['data']['uniq_Limited_nb']
    return limited_cards

def nb_rare_cards():
    rare_cards = response_json['data']['uniq_Rare_nb']
    return rare_cards

def nb_epic_cards():
    epic_cards = response_json['data']['uniq_Epic_nb']
    return epic_cards

def nb_legendary_cards():
    legendary_cards = response_json['data']['uniq_Legendary_nb']
    return legendary_cards

def total_nb_cards():
    total_cards = response_json['data']['nbTotalAnyCard']
    return total_cards

