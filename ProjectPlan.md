# Project Plan - Group 30

## Overview

Stroke is a serious and growing public health problem around the world. It happens when blood flow to the brain is blocked or reduced, and it can cause lasting brain damage, disability, or even death. Because stroke can affect people of all ages and backgrounds, it's really important to understand what puts someone at higher risk—especially when many strokes could be prevented by changing habits or getting early treatment.

Our project is focused on finding out which health conditions and everyday behaviors (like smoking, exercise, and eating habits) are linked to stroke. We want to use real data to figure out what warning signs to look for, and who might be most at risk. To do this, we’re building a data pipeline that shows how we gather, clean, combine, and analyze data in a way that others can easily follow and repeat.

We’ll use two main datasets to make our analysis stronger: one from Kaggle with patient health data in CSV format, and another from the CDC’s Behavioral Risk Factor Surveillance System (BRFSS), which we’ll access through a REST API in JSON format. These two sources give us a mix of clinical and behavioral information, and using different formats helps meet the class requirements.

In our project, we’ll go through every step of data curation. This includes collecting data with code, checking that the data is complete and trustworthy, combining data from different sources, cleaning and preparing it for analysis, doing visual and statistical analysis, and finally, saving and documenting our work. Everything we do will be shared in a private GitHub repository and written up in Markdown so it’s clear and organized.

At the end of the project, we’ll archive everything using Zenodo, which will give our project a DOI (a unique link) so that it can be shared, cited, and reused in the future. By doing all this, we hope our work will not only give useful insights into stroke risk but also serve as a good example of how to do data science projects in a reproducible and responsible way.



## Research Questions

1. **What clinical and behavioral variables are most strongly associated with stroke risk?**
2. **How can we automate the collection, cleaning, and integration of public health datasets while ensuring data quality and reproducibility?**
3. **What trends or disparities can be identified when analyzing stroke risk across different age, gender, and lifestyle groups?**

These questions drive our choice of datasets and analytical methods.


## Team Members and Roles

**Cindy Liang**
- Creates data acquisition scripts using Python (e.g., `requests` and `pandas`).
- Performs exploratory data analysis, profiling, and visualizations.
- Leads documentation efforts, writing structured Markdown files.
- Co-manages GitHub repository and reproducibility deliverables.

**Olivia Lai**
- Handles data integration (field mapping and schema matching).
- Conducts data cleaning and quality assessment.
- Builds Snakemake workflow and manages the automation of the full pipeline.
- Archives the project to Zenodo and creates metadata.

Both team members will work collaboratively on interpretation, modeling, and final write-up.




## Datasets

### 1. Stroke Prediction Dataset (CSV)
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Original Data Source (Traced):** Derived from real patient data by a healthcare analytics group.
- **Description:** 5,110 samples with demographic, health, and lifestyle features.
- **Format:** CSV
- **License:** CC0 1.0 (Public Domain)

### 2. CDC Behavioral Risk Factor Surveillance System (JSON via API)
- **Source:** CDC API at [https://chronicdata.cdc.gov](https://chronicdata.cdc.gov)
- **Description:** Annual health survey from U.S. residents covering smoking, alcohol use, physical activity, etc.
- **Format:** JSON (accessed programmatically via REST API)
- **License:** Public Domain (U.S. Federal Government)



## Data Acquisition and Integrity
-  We’ll collect the data using scripts written in Python. The Kaggle dataset will be read using pandas, and the CDC data will be downloaded from their API using requests.
- To make sure the files are correct and haven’t been changed, we’ll use SHA-256 checksums. These will be saved in a file called checksums.txt and checked when the data is loaded.
- The actual datasets will not be uploaded to GitHub. Instead, we’ll include scripts and instructions that show how to download them.
- All data collection will be handled by a script called get_data.py, and we’ll explain everything in the README.


## Data Integration and Cleaning

- Using `pandas`, we will align fields like age, gender, smoking status, and BMI between datasets.
- Integration will involve handling different naming conventions, data types, and missing value patterns.
- Cleaning steps will be documented and partially automated using OpenRefine (with JSON recipe exported).
- Manual transformations will also be described in the project’s Markdown documentation.



## Analysis and Visualization

- We will implement simple exploratory analysis and visualizations (e.g., stroke rate by age group, gender, and smoking status).
- Statistical modeling (e.g., decision trees or logistic regression) may be explored to assess feature importance.
- All visualizations will be generated using Python libraries like Matplotlib and Seaborn.
- Findings will be presented in the final README report and visual outputs saved to Box for download.



## Reproducibility and Automation

- A `Snakefile` will automate the workflow from data acquisition to visualization.
- A `run_all.sh` bash script will allow others to reproduce our analysis in one command.
- A `requirements.txt` file will specify all Python dependencies.
- Our results and metadata will be archived via Zenodo with a DOI.



## Metadata and Citation

- We will generate:
  - **Descriptive metadata** (using DataCite JSON or Schema.org format).
  - **Data dictionary** in Markdown format (explaining field names, types, units, etc.).
- All datasets and third-party tools/libraries will be cited in the README using proper citation standards (APA or DataCite).




## GitHub Repository

- A new **private GitHub repository** has been created under the `illinois-data-curation` organization:  
  `is477-sp25-Group-30`
- All team members have been added with push access.
- Work will be checked in using structured directories (e.g., `src/`, `docs/`, `data/`, `results/`).
- GitHub tags will be used to create releases for project milestones (e.g., `project-plan`, `status-report`, `final-project`).




## Timeline

| Date       | Task                                                        | Assigned To        |
|------------|-------------------------------------------------------------|--------------------|
| Apr 2      | Submit ProjectPlan.md + GitHub setup                        | Cindy & Olivia     |
| Apr 5-8    | Write and test data acquisition scripts                     | Cindy              |
| Apr 9-11   | Integrate datasets and validate schema                      | Olivia             |
| Apr 12-14  | Implement Snakemake pipeline and test reproducibility       | Olivia             |
| Apr 15     | Submit StatusReport.md                                      | Cindy & Olivia     |
| Apr 16-20  | Perform EDA and statistical analysis                        | Cindy              |
| Apr 21-25  | Create final visualizations and write findings              | Olivia             |
| Apr 26-29  | Finalize README, metadata, archive to Zenodo                | Cindy & Olivia     |
| May 1      | Submit final GitHub release                                 | Cindy & Olivia     |
| May 6      | Submit optional grad essay (if applicable)                  | N/A                |

