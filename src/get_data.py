# src/get_data.py

import os
import requests
import pandas as pd
import hashlib

# Paths
KAGGLE_CSV_PATH = 'data/stroke_data.csv'
CDC_JSON_PATH = 'data/cdc-data.json'
CHECKSUM_PATH = 'data/checksums.txt'

# CDC API Endpoint (limit: 1000 rows)
CDC_API_URL = 'https://data.cdc.gov/resource/hn4x-zwk7.json'

def download_kaggle_dataset():
    print("Checking Kaggle dataset...")
    if not os.path.exists(KAGGLE_CSV_PATH):
        raise FileNotFoundError(
            "Kaggle dataset not found. Please manually download the stroke dataset "
            "from https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset "
            "and place it at 'data/stroke-data.csv'"
        )
    print("Kaggle dataset found.")

def download_cdc_data():
    print("Downloading CDC dataset (limit 1000 rows)...")
    response = requests.get(CDC_API_URL, params={"$limit": 1000})
    print("Status code:", response.status_code)
    if response.status_code == 200:
        with open(CDC_JSON_PATH, 'w') as f:
            f.write(response.text)
        print("CDC dataset downloaded successfully.")
    else:
        print("Response text:", response.text)
        raise Exception("Failed to download CDC dataset")

def generate_checksums():
    print("Generating SHA-256 checksums...")
    with open(CHECKSUM_PATH, 'w') as f:
        for filepath in [KAGGLE_CSV_PATH, CDC_JSON_PATH]:
            with open(filepath, 'rb') as file_data:
                checksum = hashlib.sha256(file_data.read()).hexdigest()
                f.write(f"{checksum}  {filepath}\n")
    print("Checksums saved to data/checksums.txt")

if __name__ == "__main__":
    print("Starting data acquisition...")
    download_kaggle_dataset()
    download_cdc_data()
    generate_checksums()
    print("All data steps completed successfully.")
