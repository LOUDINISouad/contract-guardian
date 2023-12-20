import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("ETHERSCAN_KEY")

if api_key is None:
    raise ValueError("API key not found in .env file")

contract_address = "0x000000000022d473030f116ddee9f6b43ac78ba3"
url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}"

response = requests.get(url)
data = response.json()

if data["status"] == "1":
    
    if "SourceCode" in data["result"][0]:
        source_code = data["result"][0]["SourceCode"]
        print("Source Code:")
        print(source_code)
    else:
        print("SourceCode key not found in data['result'][0].")
else:
    print(f"Error: {data['message']}")
