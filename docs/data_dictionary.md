# Data Dictionary: Integrated Stroke Risk Dataset

This file describes the fields in the `data/integrated_cleaned.csv` file, which merges clinical and behavioral health data from a Kaggle stroke prediction dataset and the CDC BRFSS API.

| Field Name         | Type    | Description                                                           | Possible Values / Notes                                 |
|--------------------|---------|-----------------------------------------------------------------------|----------------------------------------------------------|
| age                | float   | Age of the individual                                                 | Continuous (0–100+)                                      |
| gender             | string  | Biological sex of the individual                                      | "male", "female"                                         |
| bmi                | float   | Body Mass Index                                                       | Continuous (kg/m^2); may vary in source dataset          |
| smoking_status     | string  | Self-reported smoking behavior                                        | "never smoked", "formerly smoked", "smokes"              |
| hypertension       | int     | Indicates if the individual has hypertension                          | 0 = No, 1 = Yes                                          |
| heart_disease      | int     | Indicates if the individual has heart disease                         | 0 = No, 1 = Yes                                          |
| avg_glucose_level  | float   | Average glucose level in blood                                        | Continuous (e.g., 85.6)                                  |
| stroke             | int     | Whether the individual has had a stroke (Kaggle dataset only)         | 0 = No stroke, 1 = Stroke                                |
| gender_Male        | int     | One-hot encoded: 1 if gender is Male, 0 otherwise                      | Created via `pd.get_dummies()`                          |
| smoking_status_*   | int     | One-hot encoded smoking status fields                                 | e.g., `smoking_status_never smoked` = 1 or 0             |
