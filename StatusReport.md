# Project Overview
As mentioned in our Project Plan, the aim of this project is to examine the relationship between financial inclusion and the reduction of poverty across countries and over time. By using trusted data sources from the World Bank, our goal is to analyze whether increased access to financial services, such as the ownership of bank accounts and digital bank payments has a correlation with improvements in income equality and poverty levels across the world.

Since Milestone 2, we have made significant progress with the acquisition, cleaning and integration of our data from the Poverty & Inequality Platform (PIP) and the World Bank Findex. Through our progress, we have also refined our approach and the structure of our workflow to address the challenges we faced during our implementation. 

# Project Progress
## 1. Plan Finalization: 
We finalized the scope of our project, our research questions, and the overall structure of our workflow. Our project follows a data lifecycle approach, which includes steps like the acquisition, storage, cleaning, integration, analysis, and visualization of data.

## 2. Ethical Review of Handling Data: 
Prior to acquiring data from the PIP and Findex datasets, we reviewed the ethicality of handling this data. 
- Both datasets are publically available and are open to being used for research purposes
- The dataset lacks personally identifiable information

From the above reasons, it is evident that these datasets are free to use. 

## 3. Data Organization: 
To ensure that data is organized in clear directories, we created repositories. Paths can be found below: 
- is477-project/data/raw
- is477-project/data/processed
- is477-project/scripts
- is477-project/docs
- is477-project/output

## 4. Data Acquisition: 
Post ethical review, we successfully downloaded both datasets from: 
- World Bank Global Findex Database
- World Bank Poverty and Inequality Platform

Both datasets were stored in their raw and untouched format to ensure that the integrity of the data is maintained. Path of raw data can be found below: 
- is477-project/data/raw/GlobalFindexDatabase2025.csv
- is477-project/data/raw/pip_dataset.csv

## 5. Metadata and Dataset Documentation 
We documented the URLs of sources of the Findex and PIP datasets as well as defined the variables seen across the datasets. Path to this file can be found below: 
- is477-project/docs/metadata_documentation

## 6. Data Quality Assessment and Cleaning: 
We assessed both datasets to identify: 
- Missing values
- Irrelevant variables
- Inconsistent naming conventions

After the quality assessment, we removed rows with missing required fields, such as country code and other key indicators. We also converted the data types to ensure that they were consistent across the datasets. Finally, we filtered down our data so it would simply contain the relevent variables to our analysis.

The cleaned datasets are stored in the following paths: 
- is477-project/data/processed/findex_cleaned_2024
- is477-project/data/processed/findex_cleaned_timeseries
- is477-project/data/processed/pip_cleaned_2024
- is477-project/data/processed/pip_cleaned/timeseries

A key finding of this stage was that the Findex is not updated each year, but rather every few years, which required an alteration to our integration strategy.

## 8. Data Integration: 
Using the country code and year variables as keys, we merged the cleaned datasets together. The path for the integrated datasets are: 
- is477-project/data/processed/integrated_timeseries
- is477-project/data/processed/integrated_2024

# Updated Timeline
|Task|Status|Timeline|
|----|-----------|--------|
|Plan Finalization|Completed|Week 1|
|Ethical Review|Completed|Week 1|
|Data Organization|Completed|Week 1|
|Data Acquisition|Completed|Week 2|
|Metadata and Dataset Documentation|Completed|Week 2|
|Data Quality Assessment and Cleaning|Completed|Week 2|
|Data Integration|Completed|Week 3|
|Exploratory Data Analysis|Not Started|Week 4-5|
|Final Analysis|Not Started|Week 5-6|
|Final Report|Not Started|Week 6|

# Changes to Project Plan
INFO

# Challenges and Solutions
INFO

# Individual Contributions
### Harsha Venkatnarayan
INFO

### Elizabeth Rosenberger
INFO

# Next Steps
INFO
