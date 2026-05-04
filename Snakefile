# =============================================================================
# Snakefile - Financial Inclusion & Poverty End-to-End Pipeline
# =============================================================================
# Detailed DAG with separate branches for each dataset and analysis type
# =============================================================================

rule all:
    input:
        # 2024 Cross-sectional analysis outputs
        "output/BankOwnership-Poverty2024Scatter.png",
        "output/MobileAccount-Poverty2024Scatter.png",
        "output/DigitalOwnership-Poverty2024Scatter.png",
        "output/DigitalAccess-Poverty2024Comparison.png",
        # Timeseries analysis outputs
        "output/TimeseriesGlobalTrendsPlot.png",
        "output/AveragedTimeseriesFinancialAccess-PovertyComparison.png",
        # Statistical outputs
        "output/correlation_analysis.csv",
        "output/regression_results.txt"


# =============================================================================
# PIP DATASET BRANCH - World Bank Poverty data
# =============================================================================

rule clean_pip_2024:
    input:
        pip_raw = "data/raw/pip_dataset.csv"
    output:
        pip_2024 = "data/processed/pip_cleaned_2024.csv"
    shell:
        "cd scripts && python pip2024cleaning.py --year 2024 --output ../data/processed/pip_cleaned_2024.csv"


rule clean_pip_timeseries:
    input:
        pip_raw = "data/raw/pip_dataset.csv"
    output:
        pip_ts = "data/processed/pip_cleaned_timeseries.csv"
    shell:
        "cd scripts && python pip2024cleaning.py --timeseries --output ../data/processed/pip_cleaned_timeseries.csv"


# =============================================================================
# FININDEX DATASET BRANCH - Global Findex financial inclusion data
# =============================================================================

rule clean_findex_2024:
    input:
        findex_raw = "data/raw/GlobalFindexDataset2025.csv"
    output:
        findex_2024 = "data/processed/findex_cleaned_2024.csv"
    shell:
        "cd scripts && python findex2024cleaning.py --year 2024 --output ../data/processed/findex_cleaned_2024.csv"


rule clean_findex_timeseries:
    input:
        findex_raw = "data/raw/GlobalFindexDataset2025.csv"
    output:
        findex_ts = "data/processed/findex_cleaned_timeseries.csv"
    shell:
        "cd scripts && python findex_cleaning_timeseries.py --output ../data/processed/findex_cleaned_timeseries.csv"


# =============================================================================
# MERGING STAGE - Combine PIP and Findex datasets
# =============================================================================

rule merge_2024_cross_sectional:
    input:
        pip_2024 = "data/processed/pip_cleaned_2024.csv",
        findex_2024 = "data/processed/findex_cleaned_2024.csv"
    output:
        master_2024 = "data/processed/master_dataset_2024.csv"
    shell:
        "cd scripts && python 2024merging.py --cross-sectional --output ../data/processed/master_dataset_2024.csv"


rule merge_timeseries:
    input:
        pip_ts = "data/processed/pip_cleaned_timeseries.csv",
        findex_ts = "data/processed/findex_cleaned_timeseries.csv"
    output:
        master_ts = "data/processed/master_timeseries_dataset.csv"
    shell:
        "cd scripts && python 2024merging.py --timeseries --output ../data/processed/master_timeseries_dataset.csv"


# =============================================================================
# ANALYSIS - 2024 Cross-sectional
# =============================================================================

rule analyze_2024_cross_sectional:
    input:
        master_data = "data/processed/master_dataset_2024.csv"
    output:
        scatter_bank = "output/BankOwnership-Poverty2024Scatter.png",
        scatter_mobile = "output/MobileAccount-Poverty2024Scatter.png",
        scatter_digital = "output/DigitalOwnership-Poverty2024Scatter.png",
        comparison = "output/DigitalAccess-Poverty2024Comparison.png",
        correlation = "output/correlation_analysis.csv"
    shell:
        "cd scripts && python merged_2024_analysis.py --input ../data/processed/master_dataset_2024.csv --output-dir ../output"


# =============================================================================
# ANALYSIS - Timeseries
# =============================================================================

rule analyze_timeseries:
    input:
        master_ts = "data/processed/master_timeseries_dataset.csv"
    output:
        global_trends = "output/TimeseriesGlobalTrendsPlot.png",
        avg_comparison = "output/AveragedTimeseriesFinancialAccess-PovertyComparison.png",
        regression = "output/regression_results.txt"
    shell:
        "cd scripts && python merged_timeseries_analysis.py --input ../data/processed/master_timeseries_dataset.csv --output-dir ../output"
