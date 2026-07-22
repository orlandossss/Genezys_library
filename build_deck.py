import requests
import os
from dotenv import load_dotenv
from user_info import get_user_id
load_dotenv()
token = os.getenv("Genezeys_token")


querystring = {"language":"FR"}
url = "https://app.genezys.xyz/api-prod-fantasy-game-service/decks"

querystring = {"language":"FR"}


headers = {
    "Accept": "application/json",
    "Authorization": f'{token}',
    "Referer": "https://app.genezys.xyz/",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"150\", \"Google Chrome\";v=\"150\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"
}

user_id = get_user_id()

def build_deck_division(card_info):
    cards_summaries = []
    for card in card_info:
        card_id = card['id']
        card_collection_id = card['collectionId']
        equipment_id = card.get('equipmentId', None)

        if equipment_id is None:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "isLinkedUser": True
            }
        else:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "equipmentId": equipment_id,
                "isLinkedUser": True
            }
        
        cards_summaries.append(card_summary)


    payload = {
        "cardsSummary": cards_summaries,
        "actif": True,
        "userId": user_id,
        "compatibility": {
            "leagueType": "division",
            "hash": "7d06fd0f44eceb7a9731e554f8dda962"
        }
    }
    
    response = requests.put(url, json=payload, headers=headers, params=querystring)
    
    return response.json()['message']

def build_deck_commun_cup(card_info):
    cards_summaries = []
    for card in card_info:
        card_id = card['id']
        card_collection_id = card['collectionId']
        equipment_id = card.get('equipmentId', None)

        if equipment_id is None:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "isLinkedUser": True
            }
        else:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "equipmentId": equipment_id,
                "isLinkedUser": True
            }
        
        cards_summaries.append(card_summary)


    payload = {
        "cardsSummary": cards_summaries,
        "actif": True,
        "userId": user_id,
        "compatibility":{
        "leagueType":"cup",
        "data":{
        "acceptedRarities":["common"]
        },
        "hash":"ebd84812d34db552d0e49d8b77ac2da2"}
    }
    
    response = requests.put(url, json=payload, headers=headers, params=querystring)
    
    return response.json()['message']
    

def build_deck_limited_cup(card_info):
    cards_summaries = []
    for card in card_info:
        card_id = card['id']
        card_collection_id = card['collectionId']
        equipment_id = card.get('equipmentId', None)

        if equipment_id is None:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "isLinkedUser": True
            }
        else:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "equipmentId": equipment_id,
                "isLinkedUser": True
            }
        
        cards_summaries.append(card_summary)


    payload = {
        "cardsSummary": cards_summaries,
        "actif": True,
        "userId": user_id,
        "compatibility":{
        "leagueType":"cup",
        "data":{
        "acceptedRarities":["common", 'Limited']
        },
        "hash":"35492e16883de04d62263ac46ccc7648"}
    }
    
    response = requests.put(url, json=payload, headers=headers, params=querystring)
    
    return response.json()['message']
    
def build_deck_rare_cup(card_info):
    cards_summaries = []
    for card in card_info:
        card_id = card['id']
        card_collection_id = card['collectionId']
        equipment_id = card.get('equipmentId', None)

        if equipment_id is None:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "isLinkedUser": True
            }
        else:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "equipmentId": equipment_id,
                "isLinkedUser": True
            }
        
        cards_summaries.append(card_summary)


    payload = {
        "cardsSummary": cards_summaries,
        "actif": True,
        "userId": user_id,
        "compatibility":{
        "leagueType":"cup",
        "data":{
        "acceptedRarities":["common", 'Limited', 'Rare']
        },
        "hash":"30ae6f71f9b1faaa705a0331cb9fbeff"}
    }
    
    response = requests.put(url, json=payload, headers=headers, params=querystring)
    
    return response.json()['message']

def build_deck_epic_cup(card_info):
    cards_summaries = []
    for card in card_info:
        card_id = card['id']
        card_collection_id = card['collectionId']
        equipment_id = card.get('equipmentId', None)

        if equipment_id is None:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "isLinkedUser": True
            }
        else:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "equipmentId": equipment_id,
                "isLinkedUser": True
            }
        
        cards_summaries.append(card_summary)


    payload = {
        "cardsSummary": cards_summaries,
        "actif": True,
        "userId": user_id,
        "compatibility":{
        "leagueType":"cup",
        "data":{
        "acceptedRarities":["common", 'Limited', 'Rare', 'Epic']
        },
        "hash":"1d2ed7708f26e5caa8a82b869c1cbcf8"}
    }
    
    response = requests.put(url, json=payload, headers=headers, params=querystring)
    
    return response.json()['message']

def build_deck_legendary_cup(card_info):
    cards_summaries = []
    for card in card_info:
        card_id = card['id']
        card_collection_id = card['collectionId']
        equipment_id = card.get('equipmentId', None)

        if equipment_id is None:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "isLinkedUser": True
            }
        else:
            card_summary = {
                "id": card_id,
                "collectionId": card_collection_id,
                "equipmentId": equipment_id,
                "isLinkedUser": True
            }
        
        cards_summaries.append(card_summary)


    payload = {
        "cardsSummary": cards_summaries,
        "actif": True,
        "userId": user_id,
        "compatibility":{
        "leagueType":"cup",
        "data":{
        "acceptedRarities":["common", 'Limited', 'Rare', 'Epic', 'Legendary']
        },
        "hash":"9b882b4a63286502953292996298ecb8"}
    }
    
    response = requests.put(url, json=payload, headers=headers, params=querystring)
    
    return response.json()['message']