import os

import requests
from dotenv import load_dotenv


load_dotenv()

ALCHEMY_KEY = os.getenv("ALCHEMY_KEY")
url = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_KEY}"

headers = {
    "Content-Type": "application/json",
}

data = {
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 0,
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
