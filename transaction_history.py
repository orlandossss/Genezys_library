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


def get_transaction_history(numberof_matches=10):
    url = f"https://app.genezys.xyz/api-prod-transaction-service/transactions?maxResults={numberof_matches}&language=FR"

    response = requests.get(url, data=payload, headers=headers, params=querystring)

    response_json = response.json()
    transaction_history = response_json['data']['transactionsList']

    transaction_history_info = []

    for transaction in transaction_history:
        date = transaction['created']
        type = transaction['origin']
        details = transaction['products']

        transaction_info = {
            'date': date,  
            'type': type,
            'details': details
        }

        transaction_history_info.append(transaction_info)

    return transaction_history_info
    