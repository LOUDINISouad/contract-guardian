import pandas as pd


def get_dataset():
   return pd.read_csv("data.csv")

if __name__ == "__main__":
 
    df = get_dataset()
   #print(df.columns)

    bytecode_column = df['bytecode']
    for bytecode in bytecode_column:
        print(bytecode)
      