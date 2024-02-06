from preprocess import get_raw_dataset, expand_array
from train import train_model

def main():
    
    try:
        raw_df = get_raw_dataset()
        expanded_df = expand_array(raw_df)
        expanded_df.to_csv("data.csv", index=False)
       
    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")

    
    try:
        train_model()
    except Exception as e:
        print(f"An error occurred during model training: {e}")

if __name__ == "__main__":
    main()
