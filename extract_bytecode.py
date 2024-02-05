import os
from dotenv import load_dotenv
import requests

def extract_bytecode(contract_address):
    load_dotenv()
    api_key = os.getenv("ETHERSCAN_KEY")

    if api_key is None:
        raise ValueError("API key not found in .env file")

    url = f"https://api.etherscan.io/api?module=proxy&action=eth_getCode&address={contract_address}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    print("Response:")
    print(data)

    if data["status"] == "1":
        bytecode = data["result"]
        print("Bytecode:")
        print(bytecode)
    else:
        print(f"Error: {data['message']}")

if __name__ == "__main__":
    contract_address = "0x000000000022d473030f116ddee9f6b43ac78ba3"
    extract_bytecode(contract_address)
