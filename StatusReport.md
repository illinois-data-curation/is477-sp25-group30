# Status Report – Group 30  
**Project Title: Identifying Stroke Risk Factors with Clinical and Behavioral Data**

---

## 1. Task Updates and Repository Artifacts

### Project Planning and Repository Setup  
At the beginning of the project, we completed the `ProjectPlan.md` and submitted it on time. The plan outlines our objectives, datasets, tools, workflow structure, and project timeline. We created a private GitHub repository under the `illinois-data-curation` organization titled `is477-sp25-Group-30`. The repository follows a clear and organized folder structure, including `src/` for scripts, `data/` for raw data (or links to it), `docs/` for documentation, and `results/` for outputs and visualizations.  
We also tagged the repository with `project-plan` to track progress and allow for easier navigation between project stages.

### Data Acquisition  
The data acquisition stage has been completed successfully. We used a Python script called `get_data.py`, located in the `src/` directory, to automate the retrieval of two datasets. The Kaggle stroke dataset is read using `pandas`, and the CDC dataset is accessed via a REST API using the `requests` library. Both datasets are handled in formats required by the course—CSV and JSON respectively.  

To ensure data integrity, we generated SHA-256 checksums for the downloaded files. These are stored in `data/checksums.txt`. The data files themselves are not uploaded to GitHub to follow ethical and reproducibility guidelines, but we provided instructions and scripts so users can re-download the data themselves. The process is explained in our `README.md`, along with notes on how to run the script.

### Data Integration and Cleaning  
Data integration was led by Olivia. We wrote `integrate_data.py` in `src/`, which handles schema matching between the two datasets. Variables such as `age`, `gender`, `bmi`, and `smoking_status` were aligned. This step involved converting column names, adjusting data types, and reconciling missing value formats.

We also used OpenRefine for more detailed cleaning tasks like handling null values, normalizing categorical fields, and fixing inconsistencies in the datasets. We exported a cleaning recipe in JSON format (`docs/openrefine_recipe.json`) so that others can repeat our steps. Any manual adjustments not possible through code or OpenRefine were documented in `docs/cleaning_notes.md`. We also created a snapshot of the integrated dataset and stored it locally for analysis.

### Snakemake Workflow and Automation (In Progress)  
We started implementing our reproducible workflow using Snakemake. A `Snakefile` has been created in the repository root. Currently, it automates data downloading, integration, and cleaning. We plan to expand it to include exploratory analysis and visualization steps.  

To make the pipeline easy to run, we’re developing a shell wrapper script called `run_all.sh` that will allow users to reproduce our full workflow with one command. A `requirements.txt` file listing all dependencies has been created to support reproducibility.

However, this automation phase took slightly longer than expected due to challenges with getting rule dependencies to run smoothly. Olivia is debugging the pipeline to ensure all intermediate files are produced correctly.

### Exploratory Data Analysis (EDA) and Visualizations  
Initial EDA has been started by Cindy. Using libraries like Matplotlib and Seaborn, we’ve begun generating visualizations such as:
- Stroke rate across age groups
- Gender differences in stroke risk
- Correlation heatmaps of health variables

These visualizations are saved in the `results/eda/` folder and help us identify trends and potential features for modeling. We’ve also calculated some basic statistics (mean, median, mode, distributions) to better understand the characteristics of stroke and non-stroke populations in our data.

Cindy is currently working on scripts for basic logistic regression models. These will allow us to determine which variables are the strongest predictors of stroke risk. We may add decision trees if time allows.

### Metadata and Citation (In Progress)  
We’ve begun creating metadata following the DataCite JSON format. A draft file (`docs/metadata.json`) includes project description, keywords, contributors, and links. We are also working on a structured data dictionary (`docs/data_dictionary.md`) that lists and explains each field in our combined dataset, including its type, units, and possible values.

Final citations will be included in our `README.md` using either APA or DataCite format. This includes dataset sources, libraries used, and tools like Snakemake and OpenRefine.

### Archiving and Final Packaging  
No artifacts have been archived yet, but we’ve created a Zenodo account and are preparing for final archiving. We will upload our cleaned datasets, scripts, results, and metadata. Once uploaded, Zenodo will generate a DOI that we can include in our final report and GitHub README.  
The Zenodo archiving and tagging of the final GitHub release is scheduled for April 29–May 1.

---

## 2. Updated Timeline and Task Status

| Date       | Task                                                        | Assigned To    | Status         | Notes                                  |
|------------|-------------------------------------------------------------|----------------|----------------|----------------------------------------|
| Apr 2      | Submit ProjectPlan.md + GitHub setup                        | Cindy & Olivia | ✅ Completed    |                                        |
| Apr 5–8    | Write and test data acquisition scripts                     | Cindy          | ✅ Completed    | `get_data.py` finalized and tested     |
| Apr 9–11   | Integrate datasets and validate schema                      | Olivia         | ✅ Completed    | `integrate_data.py`, OpenRefine recipe |
| Apr 12–14  | Implement Snakemake pipeline and test reproducibility       | Olivia         | 🔄 In Progress  | Partial completion, debugging ongoing  |
| Apr 15     | Submit StatusReport.md                                      | Cindy & Olivia | ✅ Completed    | This report                            |
| Apr 16–20  | Perform EDA and statistical analysis                        | Cindy          | 🔄 In Progress  | Visualization and modeling underway    |
| Apr 21–25  | Create final visualizations and write findings              | Olivia         | ⏳ Upcoming     |                                        |
| Apr 26–29  | Finalize README, metadata, archive to Zenodo                | Cindy & Olivia | ⏳ Upcoming     |                                        |
| May 1      | Submit final GitHub release                                 | Cindy & Olivia | ⏳ Upcoming     |                                        |
| May 6      | Submit optional grad essay (if applicable)                  | N/A            | ⏳ Optional     |                                        |

---

## 3. Project Plan Changes and Reflections

Throughout the project so far, our general plan has stayed on track, but a few adjustments were made:

1. **Snakemake Workflow Timeline Extended**  
We initially expected the full automation to be completed by mid-April, but dependency errors in Snakemake slowed us down. We are still working to finalize the rules, especially for analysis and visualization. As a result, we extended the workflow testing phase through April 20 and plan to add final plots by April 25.

2. **Metadata and Citation Work Shifted Later**  
While we planned to begin metadata and citation work earlier, we prioritized EDA and cleaning first. The metadata files are now being developed in parallel with our final reporting phase.

3. **Refined Modeling Approach**  
Initially, we weren’t sure if modeling would be part of the project. Based on the patterns emerging in our EDA, we now plan to use **logistic regression** to evaluate the influence of behavioral and clinical features on stroke risk. This method is easier to interpret and suitable for our goal of feature importance evaluation.

4. **Improved Collaboration and GitHub Practices**  
Throughout the project, both team members contributed actively to the repository. We used GitHub issues to track bugs and progress, and committed code with clear messages and version tags. This helped keep the project reproducible and well-organized.

---

## Final Thoughts  
So far, we are happy with how our project has progressed. We’ve successfully collected, integrated, and partially analyzed our data. Our next steps are to finish the visualizations, finalize metadata, test our workflow, and prepare the final archive. We are confident that we’ll be able to deliver a high-quality, reproducible project that meets the learning goals of this course and gives insight into public health risks related to stroke.
