import os
import requests
from dotenv import load_dotenv
from preprocess import get_raw_dataset, expand_array
from train import train_model

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

# Preprocess the raw_data.csv file
try:
    raw_df = get_raw_dataset()
    expanded_df = expand_array(raw_df)
    expanded_df.to_csv("data.csv", index=False)
   
except Exception as e:
    print(f"An error occurred during preprocessing: {e}")

# Train the model
try:
    train_model()
except Exception as e:
    print(f"An error occurred during model training: {e}")
