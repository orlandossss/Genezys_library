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

url = "https://app.genezys.xyz/api-prod-user-service/users/connected"    

def get_gnz():


    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    gnz = response_json['data']['points']['nbTokens']

    return gnz

def get_gems():


    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    gems = response_json['data']['points']['nbGems']

    return gems

def get_activity_points():


    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    activity_points = response_json['data']['points']['tokensToClaim']['nbActivityPointsOnGoingPeriod']

    return activity_points

def get_airdrop():


    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    airdrop = response_json['data']['points']['tokensToClaim']['nbTokens']

    return airdrop

def get_username():

    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    username = response_json['data']['pseudo']
    return username

def get_user_id():

    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    user_id = response_json['data']['id']
    return user_id
