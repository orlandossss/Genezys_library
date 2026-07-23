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


def get_match_history(numberof_matches=10):
    url = f"https://app.genezys.xyz/api-prod-fantasy-game-service/match/division?maxResults={numberof_matches}&language=FR"

    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    match_history = response_json['data']['matches']

    match_history_info = []
    for match in match_history:
        date = match['created']
        detail_match = match['matchSimulation']
        victory = match['userWin']
        opponnent_name = match['adversaryPseudo']
        opponent_id = match['adversaryId']
        opponent_score = match['adversaryDeck']['scoreDeck']
        user_score = match['userDeck']['scoreDeck']

        userdeck = []
        for card in match['userDeck']['cardsEquipments']:
            card_name = card['card']['clientName']
            score = card['score']
            health = card['card']['health']['points']

            card_info = {
                'card_name': card_name,
                'score': score,
                'health': health
            }

            userdeck.append(card_info)

        opponentdeck = []
        for card in match['adversaryDeck']['cardsEquipments']:
            card_name = card['card']['clientName']
            score = card['score']
            health = card['card']['health']['points']

            card_info = {
                'card_name': card_name,
                'score': score,
                'health': health
            }

            opponentdeck.append(card_info)

        match_history_info.append({
            'date': date,
            'detail_match': detail_match,
            'victory': victory,
            'opponnent_name': opponnent_name,
            'opponent_score': opponent_score,
            'opponent_id': opponent_id,
            'user_score': user_score,
            'userdeck': userdeck,
            'opponentdeck': opponentdeck
        })
    return match_history_info





