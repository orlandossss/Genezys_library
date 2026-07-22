import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("Genezeys_token")



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



def run_division_match():

    querystring = {"language":"FR"}
    url = "https://app.genezys.xyz/api-prod-fantasy-game-service/match/division/new"

    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()

    return response_json

def run_cup_match(cup_id):

    querystring = {"cupId":cup_id,"language":"FR"}
    
    url = "https://app.genezys.xyz/api-prod-fantasy-game-service/match/cup/new"

    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()

    return response_json

