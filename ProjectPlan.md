# Project Plan - Group 30

## Overview

Stroke is a major public health issue, representing one of the leading causes of long-term disability and death worldwide. Our project aims to identify key behavioral and clinical factors that contribute to stroke risk by integrating multiple data sources and building a transparent, reproducible data pipeline. Through this project, we will demonstrate how stroke-related data can be collected, curated, cleaned, analyzed, and visualized using modern data science tools and workflows.

We plan to use two different datasets: one from a Kaggle-hosted stroke dataset (CSV format) and another from the CDC's Behavioral Risk Factor Surveillance System (JSON via API). This dual-source strategy ensures that we meet the format and access method diversity requirements. Our project will include all components of data curation: acquisition with integrity checks, integration, profiling, quality assessment, cleaning, analysis, reproducibility, and archiving.

All documentation will be written in structured Markdown files and maintained in a GitHub repository following best practices. The project will also be archived using Zenodo to obtain a persistent identifier (DOI), ensuring that our results and artifacts can be accessed and cited in the future.



## Research Questions

1. **What clinical and behavioral variables are most strongly associated with stroke risk?**
2. **How can we automate the collection, cleaning, and integration of public health datasets while ensuring data quality and reproducibility?**
3. **What trends or disparities can be identified when analyzing stroke risk across different age, gender, and lifestyle groups?**

These questions drive our choice of datasets and analytical methods.

---

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



---

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


---

## Data Acquisition and Integrity

- Data will be acquired programmatically using Python's `requests` module (for the API) and `pandas` for CSV loading.
- Each dataset will be downloaded using a script (e.g., `get_data.py`) with built-in SHA-256 checksum validation.
- Checksums will be documented in `checksums.txt`.
- **Datasets will not be pushed to the GitHub repo.** Instead, documentation and code will support programmatic fetching.


---

## Data Integration and Cleaning

- Using `pandas`, we will align fields like age, gender, smoking status, and BMI between datasets.
- Integration will involve handling different naming conventions, data types, and missing value patterns.
- Cleaning steps will be documented and partially automated using OpenRefine (with JSON recipe exported).
- Manual transformations will also be described in the project’s Markdown documentation.


---

## Analysis and Visualization

- We will implement simple exploratory analysis and visualizations (e.g., stroke rate by age group, gender, and smoking status).
- Statistical modeling (e.g., decision trees or logistic regression) may be explored to assess feature importance.
- All visualizations will be generated using Python libraries like Matplotlib and Seaborn.
- Findings will be presented in the final README report and visual outputs saved to Box for download.


---

## Reproducibility and Automation

- A `Snakefile` will automate the workflow from data acquisition to visualization.
- A `run_all.sh` bash script will allow others to reproduce our analysis in one command.
- A `requirements.txt` file will specify all Python dependencies.
- Our results and metadata will be archived via Zenodo with a DOI.



---

## Metadata and Citation

- We will generate:
  - **Descriptive metadata** (using DataCite JSON or Schema.org format).
  - **Data dictionary** in Markdown format (explaining field names, types, units, etc.).
- All datasets and third-party tools/libraries will be cited in the README using proper citation standards (APA or DataCite).



---

## GitHub Repository

- A new **private GitHub repository** has been created under the `illinois-data-curation` organization:  
  `is477-sp25-Group-30`
- All team members have been added with push access.
- Work will be checked in using structured directories (e.g., `src/`, `docs/`, `data/`, `results/`).
- GitHub tags will be used to create releases for project milestones (e.g., `project-plan`, `status-report`, `final-project`).



---

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

