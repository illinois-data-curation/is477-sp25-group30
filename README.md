# Identifying Stroke Risk Factors with Clinical and Behavioral Data

## Link to Archival Record
[🔗 Zenodo DOI (replace with your link)](https://doi.org/10.0000/zenodo.placeholder)  


##  Contributors
- Cindy Liang
- Olivia [LastName]

## Summary
This project analyzes stroke risk using two datasets: a Kaggle stroke prediction dataset and the CDC Behavioral Risk Factor Surveillance System (BRFSS) API. We aimed to identify key clinical and behavioral features that contribute to stroke risk using a reproducible data science workflow.

Using Python and Snakemake, we created a pipeline to automate data acquisition, integration, cleaning, exploratory data analysis (EDA), and logistic regression modeling. The project emphasizes transparency, reproducibility, and interpretability in health data analytics.

## Research Questions
- What clinical and behavioral factors are most predictive of stroke?
- How do features such as age, BMI, smoking status, and heart disease relate to stroke risk?

## Data Profile
We used two datasets:
- **Kaggle Stroke Dataset**: 5,110 records with a `stroke` label; CSV format; manually downloaded.
- **CDC BRFSS API**: JSON data from the U.S. CDC chronic health data portal; accessed via REST API.

Common variables include `age`, `gender`, `bmi`, and `smoking_status`. Data was cleaned with Pandas and OpenRefine. Full schema is documented in [data_dictionary.md](docs/data_dictionary.md).

## Findings
- Stroke is strongly associated with age and heart disease.
- Logistic regression shows `age`, `avg_glucose_level`, and `heart_disease` have significant positive coefficients.
- Visualization shows increased stroke risk with age and among those who smoke or have chronic conditions.

## Reproducing This Project
To reproduce our workflow:

1. Clone this repo:
   ```bash
   git clone https://github.com/illinois-data-curation/is477-sp25-group30.git
   cd is477-sp25-group30
