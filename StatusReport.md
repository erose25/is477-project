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
## 1. Refining Integration Strategy: 
Our initial plan was for a simple merge of the two datasets, however, since there were missing values in the data, we decided to prioritize the quality of the data rather than simply the size of available data. 

## 2. Narrowed Selection of Key Indicators: 
We reduced the number of key variables we wanted to focus on to: 
- Bank account ownership
- Digital payments usage
- Poverty headcount ratio

## 3. Adjustments for Temporal Mismatch: 
We found that the Findex dataset only covered certain years (2011, 2014, 2017, 2021 and 2024). We updated our initial project plan to two approaches: 
- The first is to merge the data of the Findex and PIP datasets for the years 2011, 2014, 2017 and 2021 for a time series analysis based on the country code, bank account ownership, mobile money account and the poverty headcount ratio.
- The second is to merge the data of the Findex and PIP datasets for just 2024. Between 2021 and 2024, people gained access to digitally-enabled accounts. By adding this variable in the 2024 analysis, we hope to assess the impact of digitally-enabled accounts on global poverty.

# Challenges and Solutions
One major challenge involved the structure of the Poverty and Inequality Platform (PIP) dataset. The dataset contained a large number of columns (over 40), many of which were not relevant to the research question, including survey metadata, decile distributions, and auxiliary economic indicators. This made it difficult to identify which variables were necessary for analysis. To address this, the dataset was reduced to only the key variables required for the project: country_code, country_name, reporting_year, headcount, and gini. These variables were then renamed and standardized to align with the Global Findex dataset.

Another challenge was the presence of non-country observations in the PIP dataset, such as regional aggregates (e.g., “Sub-Saharan Africa” or “Europe & Central Asia”). These entries would have caused incorrect merges and misleading results if not removed. This issue was resolved by filtering the dataset to include only valid ISO 3-letter country codes.

A third challenge involved missing values in key variables such as poverty headcount and Gini coefficient. Since these variables are central to the analysis, rows with missing values were removed to ensure data quality and consistency.

A significant integration challenge arose due to differences in temporal coverage between the datasets. The Global Findex dataset is collected every few years (e.g., 2011, 2014, 2017, 2021), while the PIP dataset contains more frequent yearly observations. This mismatch initially resulted in many unmatched records during merging. To resolve this, the PIP dataset was filtered to include only years that overlap with the Global Findex dataset.

Finally, minor inconsistencies in column naming conventions (such as capitalization and spacing) caused initial merge errors. These were resolved by standardizing all column names to lowercase and ensuring consistent naming across both datasets.

# Individual Contributions
### Harsha Venkatnarayan
- Contributed to refining research questions and approach
- Analyzed and cleaned Findex dataset
- Assisted in integration of Findex and PIP datasets
- Documented proceedings and findings from Findex dataset to status report 
- Documented sources and variable definitions to Metadata and Dataset Documentation

### Elizabeth Rosenberger
- Responsible for data acquisition, preparation, and cleaning throughout the milestone
- Downloaded the Poverty and Inequality Platform (PIP) dataset and transformed it into a usable time-series format
- Selected relevant variables, renamed columns, handled missing values, removed non-country observations, and ensured consistent data types
- Implemented data integration by merging the cleaned PIP dataset with the Global Findex dataset using Python and Pandas
- Organized the repository structure (raw vs processed data), saved intermediate and final datasets, and documented the cleaning process through metadata and code comments

# Next Steps
One major challenge involved the structure of the Poverty and Inequality Platform (PIP) dataset. The dataset contained a large number of columns (over 40), many of which were not relevant to the research question, including survey metadata, decile distributions, and auxiliary economic indicators. This made it difficult to identify which variables were necessary for analysis. To address this, the dataset was reduced to only the key variables required for the project: country_code, country_name, reporting_year, headcount, and gini. These variables were then renamed and standardized to align with the Global Findex dataset.

Another challenge was the presence of non-country observations in the PIP dataset, such as regional aggregates (e.g., “Sub-Saharan Africa” or “Europe & Central Asia”). These entries would have caused incorrect merges and misleading results if not removed. This issue was resolved by filtering the dataset to include only valid ISO 3-letter country codes.

A third challenge involved missing values in key variables such as poverty headcount and Gini coefficient. Since these variables are central to the analysis, rows with missing values were removed to ensure data quality and consistency.

A significant integration challenge arose due to differences in temporal coverage between the datasets. The Global Findex dataset is collected every few years (e.g., 2011, 2014, 2017, 2021), while the PIP dataset contains more frequent yearly observations. This mismatch initially resulted in many unmatched records during merging. To resolve this, the PIP dataset was filtered to include only years that overlap with the Global Findex dataset.

Finally, minor inconsistencies in column naming conventions (such as capitalization and spacing) caused initial merge errors. These were resolved by standardizing all column names to lowercase and ensuring consistent naming across both datasets.
