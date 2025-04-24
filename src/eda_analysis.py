# src/eda_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths
INPUT_FILE = "data/integrated_cleaned.csv"
OUTPUT_DIR = "results/eda"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
df = pd.read_csv(INPUT_FILE)

# Convert types if needed
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')

# Drop any leftover NaNs
df.dropna(inplace=True)

# Summary statistics
summary = df.describe(include='all')
summary.to_csv(os.path.join(OUTPUT_DIR, "summary_statistics.csv"))
print("Saved summary statistics.")

# Visualization 1: Age Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.savefig(os.path.join(OUTPUT_DIR, "age_distribution.png"))
plt.close()

# Visualization 2: BMI Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['bmi'], bins=20, kde=True)
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.savefig(os.path.join(OUTPUT_DIR, "bmi_distribution.png"))
plt.close()

# Visualization 3: Gender Count
plt.figure(figsize=(6, 4))
sns.countplot(x='gender', data=df)
plt.title("Gender Distribution")
plt.savefig(os.path.join(OUTPUT_DIR, "gender_distribution.png"))
plt.close()

# Visualization 4: Correlation Heatmap
numeric_df = df[['age', 'bmi']].copy()
correlation = numeric_df.corr()

plt.figure(figsize=(5, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.close()

print("EDA visualizations saved to:", OUTPUT_DIR)
