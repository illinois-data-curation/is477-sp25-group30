rule all:
    input:
        "results/logistic_summary.txt",
        "results/eda/age_distribution.png",
        "results/eda/summary_statistics.csv"

rule get_data:
    output:
        kaggle="data/stroke_data.csv",
        cdc="data/cdc-data.json",
        checksums="data/checksums.txt"
    script:
        "src/get_data.py"

rule integrate_data:
    input:
        kaggle="data/stroke_data.csv",
        cdc="data/cdc-data.json"
    output:
        integrated="data/integrated_cleaned.csv"
    script:
        "src/integrate_data.py"

rule eda_analysis:
    input:
        "data/integrated_cleaned.csv"
    output:
        "results/eda/age_distribution.png",
        "results/eda/bmi_distribution.png",
        "results/eda/gender_distribution.png",
        "results/eda/correlation_heatmap.png",
        "results/eda/summary_statistics.csv"
    script:
        "src/eda_analysis.py"

rule logistic_model:
    input:
        "data/stroke_data.csv"
    output:
        "results/logistic_summary.txt"
    script:
        "src/logistic_model.py"
