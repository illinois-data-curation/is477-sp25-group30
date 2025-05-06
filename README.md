# Identifying Stroke Risk Factors with Clinical and Behavioral Data

## Link to Archival Record
[🔗 Zenodo DOI (replace with your link)](https://doi.org/10.5281/zenodo.15353241)  


##  Contributors
- Cindy Liang
- Olivia Lai
  | Date       | Task                                                        | Assigned To    | Status         | Notes                                  |
|------------|-------------------------------------------------------------|----------------|----------------|----------------------------------------|
| Apr 2      | Submit ProjectPlan.md + GitHub setup                        | Cindy & Olivia | ✅ Completed    |                                        |
| Apr 5–8    | Write and test data acquisition scripts                     | Cindy          | ✅ Completed    | `get_data.py` finalized and tested     |
| Apr 9–11   | Integrate datasets and validate schema                      | Olivia         | ✅ Completed    | `integrate_data.py`, OpenRefine recipe |
| Apr 12–14  | Implement Snakemake pipeline and test reproducibility       | Olivia         | ✅ Completed    | Partial completion, debugging ongoing  |
| Apr 15     | Submit StatusReport.md                                      | Cindy & Olivia | ✅ Completed    | This report                            |
| Apr 16–20  | Perform EDA and statistical analysis                        | Cindy          | ✅ Completed    | Visualization and modeling underway    |
| Apr 21–25  | Create final visualizations and write findings              | Olivia         | ✅ Completed    |                                        |
| Apr 26–29  | Finalize README, metadata, archive                          | Cindy & Olivia | ✅ Completed    |                                        |
| May 1      | Submit final GitHub release                                 | Cindy & Olivia | ✅ Completed    |                                        |
| May 6      | Submit optional grad essay (if applicable)                  | N/A            | ⏳ Optional     |                                        |

##  Summary

Stroke continues to be one of the leading causes of death and long-term disability worldwide. The World Health Organization estimates that approximately 15 million people suffer strokes each year, with nearly 5 million dying and another 5 million left permanently disabled. Despite medical advances, strokes remain a public health challenge, particularly due to the high costs of care and rehabilitation. Against this backdrop, early detection and preventative strategies have gained significant attention in medical research and healthcare policy. Our project contributes to this ongoing effort by exploring the application of data science and machine learning techniques to identify key risk factors for stroke.

This project is driven by the central research question: **What are the most influential clinical and behavioral predictors of stroke among adults, and how can they be interpreted in a reproducible data science workflow?** To answer this question, we used two datasets. The first is the Kaggle Stroke Prediction Dataset, which provides labeled patient data indicating whether a person had a stroke. The second is the CDC’s Behavioral Risk Factor Surveillance System (BRFSS), a large-scale health survey that provides behavioral and chronic condition data for U.S. adults.

By integrating these datasets, we aimed to capture both clinical conditions (e.g., hypertension, heart disease, glucose levels) and lifestyle factors (e.g., smoking, BMI, work type) that may contribute to stroke risk. Data integration was handled via custom Python scripts, and we used OpenRefine to assist with cleaning and normalization. Our workflow was automated using Snakemake, ensuring that the project could be easily reproduced from data acquisition to analysis.

Our methods included exploratory data analysis (EDA), visualizations, and statistical modeling. We developed a logistic regression model to determine which features had the highest statistical significance in predicting stroke. EDA plots such as age distributions, gender ratios, and correlation heatmaps helped us understand how stroke prevalence varies by demographic and clinical factors.

The project followed ethical data use principles. We avoided uploading raw data to our repository, provided SHA-256 checksums for data verification, and included scripts with documentation for re-acquisition. All code was version-controlled on GitHub, and major milestones were tagged with releases. The final output includes statistical summaries, visualizations, and modeling results.

Ultimately, our findings aligned with clinical expectations: older age, heart disease, hypertension, and elevated glucose levels are strongly associated with stroke. Smoking status and BMI had smaller but measurable effects. These results reinforce existing medical knowledge while demonstrating the power of reproducible, open-source data workflows in public health analytics.

Our project serves as a small but meaningful step toward understanding stroke risk. It also showcases how data integration, cleaning, and reproducible modeling can be applied in real-world health analytics. The next steps involve expanding the dataset, incorporating fairness analysis, and developing more sophisticated models for clinical decision-making support.



##  Data Profile

To support our analysis, we worked with two complementary datasets: the Kaggle Stroke Prediction Dataset and the CDC Behavioral Risk Factor Surveillance System (BRFSS). These datasets were selected for their richness in relevant features and their potential for integration across clinical and behavioral dimensions.

###  Kaggle Stroke Prediction Dataset

* **Source**: [https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
* **License**: Academic use only (community-shared)
* **Format**: CSV
* **Size**: 5,110 rows, 12 columns
* **Key Fields**: age, gender, hypertension, heart disease, avg\_glucose\_level, bmi, smoking\_status, stroke

This dataset includes labeled outcomes for stroke along with patient demographic, clinical, and lifestyle features. It is relatively clean but suffers from class imbalance: only about 5% of the records indicate a stroke event. Despite this, the dataset is valuable for binary classification tasks. We downloaded this data manually due to license restrictions and stored the checksum in `data/checksums.txt`. We instructed users to obtain the file themselves and documented the necessary steps.

###  CDC Behavioral Risk Factor Surveillance System (BRFSS)

* **Source**: [https://chronicdata.cdc.gov](https://chronicdata.cdc.gov)
* **License**: Public Domain (U.S. Federal Government)
* **Format**: JSON (retrieved via API)
* **Size**: Sample of \~1,000 entries
* **Key Fields**: smoking\_status, bmi, alcohol use, chronic conditions, physical activity

The BRFSS provides broader contextual data around behavioral risk factors. We used a Python script (`get_data.py`) to fetch a representative sample of this dataset using the CDC's API. This script includes integrity checks and stores the data in `data/cdc-data.json`. The dataset was helpful for comparing trends and providing complementary features to the patient-level Kaggle dataset.

###  Integration Process

Using `integrate_data.py`, we matched schema across datasets, harmonized smoking status categories, normalized BMI ranges, and removed invalid or null entries. Additional cleaning was done using Python scripts. Data was stored in `data/integrated_cleaned.csv` for further modeling.



##  Findings

Our logistic regression model produced the following key insights:

* **Age**: Strongest predictor. Stroke likelihood increases with age.
* **Heart Disease**: People with heart disease were over 3x more likely to have experienced a stroke.
* **Hypertension**: A well-known contributor, significantly associated with higher stroke probability.
* **Glucose Level**: Higher levels showed a positive correlation with stroke, aligning with diabetes risk.
* **Smoking**: Both current and former smokers had elevated risks compared to non-smokers.
* **BMI**: Surprisingly weak predictor in this dataset, potentially due to inconsistencies in source measurement.

EDA visualizations confirmed these patterns:

* Histogram of age revealed a steep increase in stroke cases after age 60.
* Gender distribution showed a slightly higher proportion of females in older stroke cases.
* Correlation matrix showed age and glucose level strongly correlated with stroke label.

Our model performed well on interpretability, though it is not optimized for predictive power. It revealed how different clinical and behavioral dimensions interact with stroke risk.



##  Future Work

While our current project met its goals, we identified several areas for future improvement:

1. **Data Expansion**: Larger, more diverse datasets could improve statistical power and enable subgroup analysis.
2. **Advanced Modeling**: Implementing Random Forests, XGBoost, or neural networks may boost predictive performance. Using SHAP or LIME could aid interpretability.
3. **Temporal Modeling**: Incorporating longitudinal data (e.g., from EMRs) would enable time-to-event analysis such as survival modeling.
4. **Bias & Fairness Analysis**: Including race, income, and region variables could reveal equity issues. Tools like Fairlearn or Aequitas can support this.
5. **Interactive Dashboards**: A user-facing app could visualize individual-level stroke risk using sliders (e.g., Streamlit or Dash).
6. **Ontology Alignment**: Mapping dataset variables to HL7 FHIR standards or SNOMED codes could improve integration with health systems.
7. **Ethics in ML**: Future studies could explore the ethical boundaries of using patient-level data for AI in diagnosis and triage.

We believe that these future directions will make the model more robust, interpretable, and relevant to both public health research and clinical practice.



##  Reproducing

To reproduce our full analysis workflow, follow these steps:

1. **Clone the GitHub repository**

```
https://github.com/illinois-data-curation/is477-sp25-Group-30
```

2. **Create a virtual environment and install dependencies**

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Manually download the Kaggle stroke dataset**

* Visit: [https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
* Download and place the CSV file in the `data/` folder as `stroke_data.csv`

4. **Run the full workflow**

```
bash run_all.sh
```

5. **View outputs**

* Logistic model summary: `results/logistic_summary.txt`
* EDA visualizations: `results/eda/*.png`
* Summary stats: `results/eda/summary_statistics.csv`

Ensure the following files are present:

* `data/stroke_data.csv`
* `data/cdc-data.json`
* `data/integrated_cleaned.csv`
* `docs/openrefine_recipe.json`
* `results/` folder with EDA and modeling results



##  References

* Fedesoriano. (2021). *Stroke Prediction Dataset*. Kaggle. [https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
* Centers for Disease Control and Prevention. (2024). *Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System*. [https://data.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7](https://data.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7)
* Statsmodels. (2024). *Statistical modeling and econometrics in Python*. [https://www.statsmodels.org/](https://www.statsmodels.org/)
* McKinney, W. (2022). *pandas: powerful Python data analysis toolkit*. [https://pandas.pydata.org](https://pandas.pydata.org)
* Koster, J. (2020). *Snakemake – a scalable bioinformatics workflow engine*. [https://snakemake.readthedocs.io](https://snakemake.readthedocs.io)
* OpenRefine. (2023). *A free, open source tool for working with messy data*. [https://openrefine.org](https://openrefine.org)
