# src/integrate_data.py

import pandas as pd
import json
import os

KAGGLE_CSV_PATH = 'data/stroke_data.csv'
CDC_JSON_PATH = 'data/cdc-data.json'
OUTPUT_PATH = 'data/integrated_cleaned.csv'

def load_kaggle_data():
    print("Loading Kaggle stroke data...")
    df = pd.read_csv(KAGGLE_CSV_PATH)
    # Standardize column names
    df.rename(columns=str.lower, inplace=True)
    return df[['age', 'gender', 'bmi', 'smoking_status']]

def load_cdc_data():
    print("Loading CDC data...")
    with open(CDC_JSON_PATH, 'r') as f:
        cdc_json = json.load(f)
    df = pd.json_normalize(cdc_json)
    
    # Make sure relevant fields exist (based on CDC format — adjust if needed)
    possible_columns = ['age', 'gender', 'bmi_value', 'smoking_status']
    df.columns = df.columns.str.lower()

    # Rename to match Kaggle
    rename_map = {
        'bmi_value': 'bmi'
    }
    df.rename(columns=rename_map, inplace=True)

    # Only keep if all needed columns are present
    keep_columns = [col for col in ['age', 'gender', 'bmi', 'smoking_status'] if col in df.columns]
    return df[keep_columns]

def clean_and_merge(kaggle_df, cdc_df):
    print("Cleaning and merging datasets...")
    combined = pd.concat([kaggle_df, cdc_df], ignore_index=True)

    # Drop missing values
    combined.dropna(inplace=True)

    # Normalize categorical data
    combined['gender'] = combined['gender'].str.lower().str.strip()
    combined['smoking_status'] = combined['smoking_status'].str.lower().str.strip()

    return combined

if __name__ == "__main__":
    kaggle_df = load_kaggle_data()
    cdc_df = load_cdc_data()
    merged_df = clean_and_merge(kaggle_df, cdc_df)

    os.makedirs('data', exist_ok=True)
    merged_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Integrated cleaned data saved to: {OUTPUT_PATH}")
