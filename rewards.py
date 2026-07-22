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





def get_daily_rewards_info():

    url = "https://app.genezys.xyz/api-prod-fantasy-game-service/daily-rewards/current"
    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()

    id = response_json['data']['id']
    reward_type = response_json['data']['rewardType']
    reward_quantity = response_json['data']['rewardQuantity']
    item_id = response_json['data']['fantasyItemDefinitionId']

    return id, reward_type, reward_quantity, item_id

def get_missions_info():
    url = "https://app.genezys.xyz/api-prod-fantasy-game-service/missions/daily"
    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    missions = response_json['data']['milestones']
    missions_info = []
    for mission in missions:
        mission_title = mission['title']
        reward_quantity = mission['rewardQuantity']
        action_quantity = mission['actionQuantity']
        reward_type = mission['rewardType']

        mission_info = {
            'title': mission_title,
            'reward_quantity': reward_quantity,
            'action_quantity': action_quantity,
            'reward_type': reward_type
        }


        missions_info.append(mission_info)

    mission_info = {
        'title': 'Finir toutes les misions',
        'reward_quantity':  response_json['data']['rewardQuantity'],
        'reward_type': response_json['data']['rewardType']
        
    }

    missions_info.append(mission_info)

    return missions_info

