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
        
        if not isinstance(bytecode, (str, bytes)):  
            bytecode = str(bytecode)

        encoded_tokens = enc.encode(bytecode)
        decoded_bytecode = enc.decode(encoded_tokens)  

        return encoded_tokens
    except Exception as e:
        print(f"Error during tokenization: {e}")
        raise e

if __name__ == "__main__":
    try:
        df = get_dataset()

        # Create a new column 'Encoded_Tokens' with the encoded tokens
        df['Encoded_Tokens'] = df['Bytecode'].apply(tokenize_bytecode)
        
        df.to_csv("data_with_tokens.csv", index=False)

    except Exception as e:
        print(f"An error occurred: {e}")
