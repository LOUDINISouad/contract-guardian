import pandas as pd
import tiktoken
import numpy as np

def get_dataset():
    try:
        return pd.read_csv("raw_data.csv")
    except FileNotFoundError as e:
        print(f"Error: Unable to find raw_data.csv file. Please ensure it's in the correct location.")
        raise e

def tokenize_bytecode(bytecode):
    try:
        enc = tiktoken.get_encoding("cl100k_base")

        if not isinstance(bytecode, (str, bytes)):
            bytecode = str(bytecode)

        encoded_tokens = enc.encode(bytecode)
        #decoded_bytecode = enc.decode(encoded_tokens)  

        return encoded_tokens
    except Exception as e:
        print(f"Error during tokenization: {e}")
        raise e

def pad_arrays(array, max_length, padding_token):
    if len(array) < max_length:
        padded_array = np.pad(array, (0, max_length - len(array)), 'constant', constant_values=padding_token)
    else:
        padded_array = array[:max_length]
    return padded_array

if __name__ == "__main__":
    try:
        df = get_dataset()

        df['encoded_tokens'] = df['bytecode'].apply(tokenize_bytecode)
        max_length = 9021
        padding_token = 0

        # Pad the arrays
        df['padded_arrays'] = df['encoded_tokens'].apply(lambda x: pad_arrays(x, max_length, padding_token))

        padded_arrays = df.pop("padded_arrays")
        tokens = pd.DataFrame(padded_arrays.tolist(), columns=[f"token_{i}" for i in range(9021)])
        df_expanded = pd.concat([df, tokens], axis=1)

        df_expanded.to_csv("data.csv", index=False)

    except Exception as e:
        print(f"An error occurred: {e}")
