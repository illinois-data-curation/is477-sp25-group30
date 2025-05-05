# src/logistic_model.py

import pandas as pd
import statsmodels.api as sm
import os

INPUT_FILE = "data/stroke_data.csv"
OUTPUT_FILE = "results/logistic_summary.txt"
os.makedirs("results", exist_ok=True)

# Load and filter dataset
df = pd.read_csv(INPUT_FILE)

# Select only relevant columns
df = df[['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
         'gender', 'smoking_status', 'stroke']]

# Drop rows with missing values and filter out 'Other' gender
df = df[df['gender'] != 'Other']
df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')
df.dropna(inplace=True)

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=['gender', 'smoking_status'], drop_first=True)

# Ensure all columns are numeric
df = df.apply(pd.to_numeric, errors='coerce')
df.dropna(inplace=True)

# Features and target
X = df.drop('stroke', axis=1).astype(float)
y = df['stroke'].astype(float)




# Add constant
X = sm.add_constant(X)
print("\n DEBUG: X dtypes:")
print(X.dtypes)
print("\n DEBUG: y dtype:")
print(y.dtype)
print("\n DEBUG: First 5 rows of X:")
print(X.head())

# Fit logistic regression
model = sm.Logit(y, X)
result = model.fit()

# Save output
with open(OUTPUT_FILE, 'w') as f:
    f.write(result.summary().as_text())

print(" Logistic regression complete. Summary saved to:", OUTPUT_FILE)
