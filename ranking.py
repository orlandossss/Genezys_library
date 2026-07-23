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

def cup_leaderboard(cup_id, max_results = 10):
    url = "https://app.genezys.xyz/api-prod-leaderboard-service/rankings/cup/overview"
    querystring = {"cupId":cup_id,"topx":max_results,"aroundx":"10","language":"FR"}
    response = requests.get(url, data=payload, headers=headers, params=querystring)
    response_json = response.json()


    personal_info = response_json['data']['me']
    personal_score = personal_info['score']
    personal_match_done = personal_info['nbMatchLaunch']
    personal_position = personal_info['position']

    own_info_cup = {
        'score': personal_score,
        'matchplayed': personal_match_done,
        'position': personal_position
    }

    players_cup = []
    for player in response_json['data']['top']:
        score = player['score']
        name = player['pseudo']
        userId = player['userId']
        match_done = player['nbMatchLaunch']
        position = player['position']

        player_info = {
            'score': score,
            'name': name,
            'userId': userId,
            'matchplayed': match_done,
            'position': position
        }

        players_cup.append(player_info)

    return own_info_cup, players_cup


def division_leaderboard(max_results):
    url = "https://app.genezys.xyz/api-prod-leaderboard-service/rankings/division/overview"
    querystring = {"topx":max_results,"aroundx":"10","language":"FR"}
    response = requests.get(url, data=payload, headers=headers, params=querystring)
    response_json = response.json()


    personal_info = response_json['data']['me']
    personal_score = personal_info['score']
    personal_match_done = personal_info['nbMatchLaunch']
    personal_position = personal_info['position']
    division_rank = personal_info['divisionRank']

    own_info_division = {
        'score': personal_score,
        'matchplayed': personal_match_done,
        'position': personal_position,
        'division_rank': division_rank
    }

    players_div = []
    for player in response_json['data']['top']:
        score = player['score']
        name = player['pseudo']
        userId = player['userId']
        match_done = player['nbMatchLaunch']
        position = player['position']

        player_info = {
            'score': score,
            'name': name,
            'userId': userId,
            'matchplayed': match_done,
            'position': position
        }

        players_div.append(player_info)

    return own_info_division, players_div