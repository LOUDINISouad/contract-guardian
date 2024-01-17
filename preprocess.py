import pandas as pd
import tiktoken

def get_dataset():
    try:
        return pd.read_csv("data.csv")
    except FileNotFoundError as e:
        print(f"Error: Unable to find data.csv file. Please ensure it's in the correct location.")
        raise e

def tokenize_bytecode(bytecode):
    try:
        enc = tiktoken.get_encoding("cl100k_base")
        if not isinstance(bytecode, (str, bytes)):  # Ensure valid data type
            raise TypeError("Input bytecode must be a string or bytes object.")

        encoded_tokens = enc.encode(bytecode)
        decoded_bytecode = enc.decode(encoded_tokens)  

        print("Original Bytecode:", bytecode)
        print("Encoded Tokens:", encoded_tokens)
        print("Decoded Bytecode:", decoded_bytecode)

        return encoded_tokens
    except Exception as e:
        print(f"Error during tokenization: {e}")
        raise e

if __name__ == "__main__":
    try:
        df = get_dataset()
        bytecode_column = df['Bytecode']

        for bytecode in bytecode_column:
            tokenize_bytecode(bytecode)
    except Exception as e:
        print(f"An error occurred: {e}")
