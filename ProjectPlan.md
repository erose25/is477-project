# Overview
The aim of this project is to examine the relationship between financial inclusion and the reduction of poverty across countries and over time. By using trusted data sources from the World Bank, our goal is to analyze whether increased access to financial services, such as the ownership of bank accounts, digital bank payments and access to financial credit, has a correlation with improvements in income equality and poverty levels across the world.

Financial inclusion is fundamental to the World Banks mission to promote sustainable economic development that trickles down all members of society. Despite the progress that society has been making over time, large disparities exist all over the world in terms of access to financial systems and education. By integrating the Global Findex Database and the Poverty and Inequality Platform, which measure financial inclusion metrics and global poverty and income inequality respectively, this project aims to uncover trends that may be able to explain the ways in which financial inclusion can help alleviate poverty. 

This project will leverage a data lifecycle model to manage the acquisition, integration, cleaning, analysis and visualization of data. We will be acquiring datasets from APIs and CSV sources, cleaning and merging them using Python's open-source Pandas library, analyzing the data and then visualizing the results to help discover insights. Our final deliverable will be a comprehensive report that will help those in charge of policy understand how having more inclusive financial systems in place could help contribute to equitable economic development.


# Team
1. Elizabeth Rosenberger:
   - Responsible for acquiring data from APIs or CSV sources and preparing and cleaning them to ensure quality and reproducibility
   - Documenting findings in final report
2. Harsha Venkatnarayan:
   - Responsible for conducting exploratory and statistical analyses and creating data visualizations
   - Documenting findings in final report


# Research Questions
As discussed in the Overview section, the goal of this project is to identify trends or causal relationships between financial inclusion and improvements in income equality and poverty reduction. Therefore, the primary question we are attempting to answer is: 
  - How does financial inclusion influence the reduction of poverty across countries and regions?

Some additional questions that we aim to answer through this project are: 
  - Does increased access to digital financial services and banking correlate with lower poverty headcounts?
  - Are there variations in financial inclusion based on gender? If so, can the explain differences in income inequality?


# Datasets
1. **World Bank Global Findex Database**
  - Source and URL: World Bank (https://www.worldbank.org/en/publication/globalfindex)
  - Access Method: Downloadable CSV file
  - Description: This database is the most comprehensive dataset on how people save, borrow and make make payments. It provides indicators on financial inclusion, income level and gender. 
2. **World Bank Poverty and Inequality Platform**
  - Source and URL: World Bank (https://pip.worldbank.org/poverty-calculator)
  - Access Method: Downloadable CSV file
  - Description: The Poverty and Inequality Platform provides global, regional and national estimates of poverty and inequality indicators. 

Both datasets have some common variables which would allow for their integration. For this project, we will be using the **Year** and **Country Code** fields to allow for a straightforward integration process. After merging the data, we will also create a master dataset with annual indicators to enable time-series and cross-sectional analyses.


# Timeline
|Task|Description|Timeline|Responsible|
|----|-----------|--------|-----------|
|Plan Finalization & Lifecycle Design| Define project scope, finalize research questions, map workflow according to Data Lifecycle requirements. | Week 1 | Both |
|Data Acquisition| Download datasets from World Bank Global Index Findex Database and Pverty and Inequality Platform.  Document data sources, access methods, and formats to satisfy Data Collection and Acquisition requirements. | Week 1 | Elizabeth |
|Storage and File Organization Setup| Create a structured repository containing folders for raw data, processed data, scripts, documentation, and results.  Define file naming conventions and data structures (CSV files and Pandas Dataframes) to meet File Storage and Organization requirements. | Week 1 | Elizabeth |
|Metadata and Dataset Documentation| Document metadata such as dataset source, schema, variable definitions, file formats, and licensing information to support Metadata and Data Documentation and Reproduceability and Provenance. | Week 2 | Elizabeth |
|Data Quality Assessment| Evaluate datasets for missing values, inconsistent country codes, duplicates, and structural inconsistencies.  Record results of the evaluation to fulfill Data Quality requirements. | Week 2 | Elizabeth |
|Data Cleaning| Apply Cleaning methods such as handling missing values, standardizing country codes, correcting formatting issues, and removing unecessary variables.  This step addresses Data Cleaning requirements within the Extraction and Enrichment stage. | Week 2-3 | Elizabeth |
|Data Integration| Merge Datasets using Python and the Pandas library by aligning shared varibales such as Country Code and Year to fulfill Data Integration requirements. | Week 3 | Elizabeth |
|Data Enrichment| Create derived indicators or additional features that improve analysis (e.g. normalized metrics or aggregated indicators), fulfilling the Extraction and Enrichment requirement. | Week 3 | Elizabeth |
|Exploratory Data Analysis | Conduct exploratory statistical analysis to identify correlations between financial inclusion indicators and poverty measures.  This step helps validate the dataset and supports future interpretation. | Week 4 | Harsha |
|Workflow Automation| Implement scripts or notebooks that automate the entire workflow (from loading raw data through data cleaning, integration and analysis) to meet Workflow Automation and Provenance requirements. | Week 4-5 | Both | 
|Ethical Data Handling Review| Review licensing terms and confirm compliance with dataset usage policies, ensuring proper citation and responsible data use according to Ethical Data Handling requirements. | Week 5 | Both | 
|Reproduceability Implementation| Ensure the workflow can be replicated by documenting scripts, dependencies, and processing steps.  This fulfills Reproduceability and Provenance requirements. | Week 5 | Both | 
|Final Analysis and Interpretation| Conduct final statistical analysis and interpret the results related to financial inclusion and poverty reduction trends. | Week 5 | Harsha | 
|Final Report and Documentation| Compile the report, including methodology, workflow documentation, results, and metadata descriptions to support Metadata and Data Documentation and overall project reproduceability. | Week 6 | Both |


# Constraints
**Temporal Coverage Differences (Global Findex Database)**
The World Bank Global Findex Database is not collected annually; instead, it is based on survey waves conducted approximately every three years (e.g., 2011, 2014, 2017, 2021). In contrast, the Poverty and Inequality Platform dataset often provides yearly estimates for poverty and inequality indicators. Because of this mismatch in reporting frequency, the project may need to align analyses only to the specific years available in the Global Findex data. This limitation could reduce the temporal resolution of the analysis.

**Missing or Incomplete Country Data (Both Datasets)**
Both the Global Findex Database and the Poverty and Inequality Platform dataset may have missing data for certain countries or years. Some countries may lack survey responses in the Global Findex data, while others may not have updated poverty estimates in the Poverty and Inequality Platform. These missing values may limit the number of countries included in the final analysis or require filtering and cleaning steps.

**Differences in Indicator Definitions (Both Datasets)**
The two datasets measure different economic and social indicators that are produced using different methodologies. The Global Findex dataset relies largely on survey-based indicators such as bank account ownership, digital payment usage, and access to financial credit. Meanwhile, the Poverty and Inequality Platform dataset provides modeled economic indicators such as poverty headcount ratios and income inequality metrics. These methodological differences may introduce challenges when interpreting correlations between financial inclusion and poverty reduction.

**Data Integration Challenges (Both Datasets)**
Although both datasets contain Country Code and Year variables that allow integration, inconsistencies may still arise. For example, some countries may use slightly different naming conventions or may have data available in one dataset but not the other for a specific year. Careful alignment and validation will be required during the data integration process.

**Ethical and Legal Considerations (Both Datasets)**
Both datasets are publicly available through the World Bank and are intended for research and policy analysis. However, the project must still comply with licensing terms and provide proper citation for all data sources. Since both datasets contain aggregated country-level statistics rather than individual-level data, privacy risks are minimal. Nonetheless, ethical handling of the data will include transparent documentation of data sources, transformations, and limitations.

**Data Interpretation Limitations (Both Datasets)**
Even if correlations are observed between financial inclusion indicators and poverty reduction metrics, the analysis may not establish direct causation. Many external factors (including government policies, economic growth, or regional development differences) may influence poverty outcomes. This limitation should be acknowledged when interpreting the results.


# Gaps
**Selection of Specific Indicators**
Both datasets contain many variables. We will need to identify which financial inclusion indicators (e.g., bank account ownership, digital payment usage, access to credit) and which poverty indicators (e.g., poverty headcount ratio, Gini coefficient) are most relevant for analysis.

**Statistical Method Selection**
The project currently proposes exploratory analysis and correlation analysis, but additional statistical techniques such as regression analysis may be explored depending on the structure of the merged dataset.

**Data Transformation Strategy**
It is not yet fully determined whether the analysis will rely on raw indicators or normalized metrics (e.g., per capita or percentage-based transformations).

**Visualization Design**
The specific types of visualizations that will best communicate the results (e.g., time-series graphs, geographic maps, or comparative bar charts) will be finalized after exploratory analysis.

**Workflow Implementation**
While the workflow will be automated using Python scripts or Jupyter notebooks, the exact implementation details (such as modular scripts or a pipeline structure) will be determined during development.


# Conclusion
INFO
