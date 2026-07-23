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

url = "https://app.genezys.xyz/api-prod-challenge-service/challenges"

response = requests.get(url, data=payload, headers=headers, params=querystring)

response_json = response.json()

def get_challenges_info():
    challenge_info = []
    for challenge in response_json['data']:

        name = challenge['title']
        athlete = challenge['clientName']
        total_entries = challenge['nbTotalEntries']
        start_date = challenge['challengeStartAt']
        end_date = challenge['challengeEndAt']

        challenge_info.append({
            'name': name,
            'athlete': athlete,
            'total_entries': total_entries,
            'start_date': start_date,
            'end_date': end_date,
            })   
    
    return challenge_info


