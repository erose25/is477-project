# Global Financial Inclusion and Poverty Reduction Analysis

## Contributors 
- Harsha Venkatnarayan
- Elizabeth Rosenberger

## Summary
This project analyzes the relationship between financial inclusion and literacy and poverty reduction across countries and over time. Financial inclusion in this project can be defined as access to financial services such as bank accounts, digital payments, and credit. The primary research question that is guiding this project is: 

*How does financial inclusion influence the reduction of poverty across countries and regions?*

In an effort to answer this question, we integrated data from the Global Findex Database as well as the Poverty and Inequality Platform (PIP). The Findex dataset contains indicators from surveys that such as percentage of account ownership and digital financial account usage across countries, while the PIP dataset contains poverty headcount ratios across countries. 

We followed a methodology in line with a full data lifecycle approach, which includes steps like data acquisition, cleaning, integration, analysis, and visualization. Post data acquisition and cleaning, we created master datasets for a time-series analysis as well as an analysis for the year 2024. 

To address differences in data across time, we also conducted:
- Time-series analysis (2014–2021) using overlapping years
- Point-in-time analysis (2024) which included digital financial indicators missing in earlier years

Additionally, we also created a comparative analyses between extreme cases, looking at countries with:
- High poverty against high financial inclusion
- High and low digital financial account adoption

Our key findings were in line with the inverse relationship between financial inclusion and poverty levels as we initially expected. Countries that had higher account adoption and digital financial account adoption tended to have lower poverty headcount ratios. Additionally, we also found that access to and adoption of digital financial services have played an  increasingly important role in recent years (in 2024 as compared to our time-series analysis of prior years). Countries with higher levels of digital financial account ownership tended to have lower poverty headcount ratios, which suggest that access to and adoption of digital tools may have a positive effect on economic inclusion and equity. 

However, we do want to make it clear that this analysis does not establish causation. There are other external factors like economic polivy, GDP growth and more that could also influence a country's poverty headcount ratio. Therefore, we believe that these results show more correlation than causation of our primary research question.


## Data Profile
### Global Findex Database
- Source: World Bank
- File Location: data/raw/GlobalFindexDatabase2025.csv
- Description: Provides survey-based indicators on how individuals access and use financial services through variables like:
    - Account ownership (% of adults)
    - Digital payment usage
    - Mobile money account ownership
    - Country code and year
- Characteristics:
    - Collected approximately every 3 years (2011, 2014, 2017, 2021 and 2024)
    - Aggregated at the country level
    - Follows a survey-based methodology

### Poverty and Inequality Platform (PIP)
- Source: World Bank
- File Location: data/raw/pip_dataset.csv
- Description: Provides modeled estimates of poverty and inequality through variables like:
    - Poverty headcount ratio
    - Gini coefficients
    - Country code and year
- Characteristics:
    - Measured annually but has inconsistencies between countries
    - Includes regional aggregates which were removed during cleaning steps

### Ethical and Legal Considerations
- Both datasets are publicly available and licensed for research use
- No personally identifiable information (PII)
- Proper citation is required

## Data Quality
The integrity of this cross-country analysis relies heavily on the quality and synchronization of two distinct datasets: the World Bank Global Findex Database and the Poverty and Inequality Platform (PIP). While both are gold-standard sources for global development metrics, merging them for a longitudinal study introduced several complex data quality challenges. To ensure the reliability of our findings, we conducted a rigorous assessment of the data’s completeness, consistency, and temporal alignment.

### 1. Missing Values and Dataset Completeness
The most immediate challenge to data quality was the presence of null values across both primary indicators.
- Poverty Metrics: In the PIP dataset, reporting is not uniform across all nations every year; some countries may go several years without a household survey, leading to "gaps" in the poverty headcount ratio.
- Financial Indicators: In the Findex data, while general account ownership is widely reported, newer indicators—such as mobile money usage or digital payment frequency—were often missing for lower-income or less technologically integrated regions in earlier waves.

To maintain the statistical validity of our correlations, we opted for a listwise deletion approach for rows missing these critical variables. While this ensured that every data point used in our analysis was grounded in empirical evidence, it inherently reduced our total sample size and potentially filtered out countries with the most severe infrastructure challenges, where data collection is most difficult.

### 2. Temporal Mismatch and Periodicity
A significant hurdle in the data integration process was the asynchronous nature of data collection between the two sources.
- Findex is triennial, providing "snapshots" of financial behavior (2011, 2014, 2017, 2021).
- PIP provides annual modeled estimates, but the underlying survey data varies by country.

This mismatch required a strategic filtering process. We treated the Findex years as our primary anchors and "binned" the PIP data to match these specific survey waves. For the 2024 cross-sectional analysis, we utilized the most recent available modeled projections from PIP. This temporal alignment is crucial; however, it introduces a "lag" risk where a country's financial inclusion metrics from early 2021 are being compared against poverty metrics modeled for the end of the same year, which may not capture rapid economic shifts caused by external shocks.

### 3. Structural Integrity and Non-Country Entities
Both World Bank datasets include "aggregate" entries that represent regional averages (e.g., "Latin America & Caribbean," "Fragile and conflict-affected situations") or income-level groupings (e.g., "Lower middle income"). Including these in a cross-country analysis would lead to double-counting and skewed results, as individual countries would be represented both as unique rows and as part of an aggregate average.
We addressed this by implementing a strict ISO-3 validation filter. By retaining only entries with valid 3-letter country codes, we ensured that the unit of analysis remained consistent and that our merges were based on distinct geopolitical entities. This step was vital for preventing the "merging noise" that often occurs when descriptive names for regions differ slightly between datasets.

### 4. Methological Divergence: Survey vs. Modeled Data
There is an inherent qualitative difference in how these data points are generated.
- Findex data is survey-based, reflecting the self-reported behaviors and perceptions of individuals.
- PIP data is modeled, often involving interpolations and "extrapolations" to fill gaps between census years.

This divergence introduces a unique interpretation challenge: we are essentially comparing subjective participation (did a person say they used a bank account?) with objective economic modeling (what is the estimated headcount ratio?). While this is the standard approach in development economics, we must acknowledge that survey bias (social desirability bias in reporting bank usage) and modeling errors in poverty estimates could introduce unobserved variance into our results.

### 5. Selection Bias in Comparative Visualization

To provide clear insights into the relationship between the variables, our visualizations often highlight "extreme cases"—countries at the polar ends of the inclusion or poverty spectrums. While this strengthens the interpretability of the inverse relationship we observed, it introduces a degree of selection bias. By focusing on the "highest" and "lowest" performers, the nuances of "middle-tier" countries—where the relationship between inclusion and poverty might be more obscured by local policy or industrial shifts—may be less visible. Consequently, while our findings show a strong global trend, the specific visualizations should be viewed as illustrative of a broader phenomenon rather than a universal rule applied to every unique economy.

By identifying and mitigating these quality issues—through rigorous cleaning, ISO validation, and temporal synchronization—we have created a robust master dataset that minimizes noise while maximizing the signal of the relationship between financial access and poverty reduction.


## Data Cleaning
Steps performed:
- Removed rows with missing key variables: For PIP, rows missing headcount_ratio were removed. For Findex, rows missing account, mobile_account, or digital_payment were removed to ensure complete cases for each country-year observation.
- Filtered only valid ISO 3-letter country codes: Both datasets contained regional aggregates (e.g., "Sub-Saharan Africa") and economic groupings. A strict filter was applied to retain only rows with valid ISO 3-letter country codes (e.g., USA, NGA, IND) to ensure accurate country-to-country merging.
- Standardized column names: Column names were converted to lowercase, spaces replaced with underscores, and prefixes/suffixes removed. For example, "Poverty Headcount Ratio at $2.15 a day (2017 PPP) (% of population)" became headcount_ratio, and "Account ownership (% of population ages 15+)" became account_ownership.
- Reduced dataset to relevant variables: PIP was reduced to country_code, reporting_year, headcount_ratio ($2.15 line), poverty_gap, and population. Findex was reduced to account_ownership, mobile_account_ownership, digital_payment_usage, saved_at_financial_institution, and borrowed_from_financial_institution.
- Converted data types: Numeric columns such as reporting_year were converted to integers, while headcount_ratio and account_ownership were converted to floats to enable mathematical operations like merging, filtering, and plotting.
- Filtered PIP to match Findex years: For time-series analysis, PIP was filtered to Findex survey waves (2014, 2017, 2021). For 2024 cross-sectional analysis, PIP was filtered to the single most recent year (2024).
- Created cleaned datasets: Two final CSV files were produced: findex_cleaned_timeseries.csv (cleaned Findex indicators for 2014, 2017, 2021, 2024) and pip_cleaned_timeseries.csv (cleaned PIP poverty measures for matching years).


## Findings
### 1. Global Time-Series Trends
- Account ownership increased between 2014 and 2021
- Mobile account usage saw a significant amount of growth over time in this period
- Poverty headcount declined from during the same period along with this increase in account ownership and usage

*Interpretation:*

Our findings indicated that there is a clear negative correlation between financial inclusion and poverty over this time period. As access to financial services increase all of the world, poverty headcount ratios tended to decrease. 

### 2. High Poverty against High Financial Inclusion Countries
To better understand differences between countries, we intentionally selected countries at opposite ends:
- High poverty countries: Zimbabwe (ZWE), Togo (TGO), Niger (NER)
- High financial inclusion and literate countries: Malaysia (MYS), Russia (RUS), South Africa (ZAF)

*Key Observations:*
- Niger shows extremely low account ownership and very high poverty
- Malaysia and Russia show high account ownership with a near-zero poverty headcount ratio
- Zimbabwe and Togo lie in the middle with moderate levels of financial access and poverty

Our analysis once again reinforced our hypothesis that with higher financial inclusion, poverty levels decrease. The contrast between our selected countries highlights how limited financial access aligns with cases of extreme poverty. 

### 3. Digital Financial Access (2024 Analysis)
Countries were selected based on ownership of digital accounts:
- High access to digial accounts: Argentina (ARG), Panama (PAN)
- Low access to digial accounts: India (IND), Tajikistan (TJK)

*Key Observations:*
- Argentina: High digital access with very low poverty levels
- Panama: Moderate digital access with low poverty levels 
- India: Lower digital access with higher poverty levels
- Tajikistan: Low digital access with moderate poverty levels

Our analysis revealed that countries with higher adoption of digital financial accounts and tools tend to have lower poverty headcount ratios. India may seem to be an exception to our found correlation, but we believe that it can be explained by broader economic factors.

### Overall Insight:
- Financial inclusion shows a strong negative relationship with poverty headcount ratios across the globe and over time
- Access to and adoption of digital financial services is an emerging factor for decreasing poverty headcount ratios

## Future Work
While this study identifies a strong inverse relationship between financial inclusion and poverty, several extensions could improve the rigor and explanatory power of the analysis.

### 1. Multivariate Regression and Controls
Future work should move beyond bivariate analysis by incorporating multivariate regression models that control for key factors such as GDP per capita, education, unemployment, and regional effects. This would help isolate the independent impact of financial inclusion and determine whether the observed relationship persists after accounting for broader economic conditions.

### 2. Causal Inference Methods
To address the limitation of correlation-based findings, future research should apply panel data methods such as fixed effects models to control for unobserved country-specific characteristics. More advanced approaches, including difference-in-differences or instrumental variables, could help establish causal links, particularly by leveraging policy changes or expansions in financial access as natural experiments.

### 3. Gender and Demographic Analysis
Expanding the analysis to include gender and demographic disparities would provide more nuanced insights. Using disaggregated indicators from the Global Findex dataset, future work could examine differences in financial access across gender, income groups, and rural versus urban populations.

### 4. Expanded Macroeconomic and Institutional Data
Incorporating additional variables, such as governance quality, financial system development, and technological infrastructure (e.g., internet access), would help account for structural differences across countries and better explain variation in poverty outcomes.

### 5. Digital Financial Services Over Time
As more data becomes available, future research should extend the analysis of digital financial inclusion over a longer time horizon. Distinguishing between types of digital services (e.g., mobile money vs. online banking) could also clarify which mechanisms are most effective in reducing poverty.

### 6. Broader Country Coverage and Robustness Checks
Including middle-income countries and conducting robustness checks, such as alternative poverty thresholds or model specifications, would improve the generalizability and reliability of findings.


## Challenges
### 1. Selection Bias from Extreme Country Comparisons
Selecting "extreme" countries improves visual clarity but introduces selection bias. To make relationships interpretable, we intentionally compared high-poverty countries (Zimbabwe, Togo, Niger) against high-financial-inclusion countries (Malaysia, Russia, South Africa). While this creates clear visualizations, the chosen countries are not representative of all nations. Readers should interpret these comparisons as illustrative examples rather than statistically representative findings.

### 2. Unobserved Structural Differences Across Countries
Cross-country comparisons may be influenced by unobserved structural differences. Factors such as governance quality, economic policy environments, infrastructure development, historical contexts, and cultural attitudes toward banking all affect poverty outcomes. Our analysis cannot control for these variables, meaning observed correlations may partially reflect underlying structural differences rather than a direct causal effect of financial inclusion.

### 3. Limited Time Scope for Digital Access Data
Digital access data is recent and limited in time scope. The Global Findex Database only began collecting detailed mobile money and digital payment indicators in recent survey rounds (primarily 2017 onward). Unlike traditional account ownership (measured since 2011), digital access indicators lack the historical depth needed for robust longitudinal analysis of long-term trends.


## Reproducing
### Step 1: Clone Repository

    git clone https://github.com/erose25/is477-project
    cd is477-project

### Step 2: Install Dependencies

    pip install -r requirements.txt

Note: For DAG visualization, Graphviz must also be installed as a system-level dependency.
- Windows: Download from graphviz.org, check "Add Graphviz to system PATH"
- macOS: brew install graphviz
- Linux: sudo apt-get install graphviz
- Verify with: dot -V

### Step 3: Place Raw Data in data/raw/

Download the two datasets from the World Bank:
- PIP Dataset from pip.worldbank.org → save as pip_dataset.csv
- Global Findex 2025 from globalfindex.worldbank.org → save as GlobalFindexDataset2025.csv

Expected folder structure:

    project/
    ├── data/raw/
    │ ├── pip_dataset.csv
    │ └── GlobalFindexDataset2025.csv
    ├── scripts/
    │ ├── pip2024cleaning.py
    │ ├── findex2024cleaning.py
    │ ├── findex_cleaning_timeseries.py
    │ ├── 2024merging.py
    │ ├── merged_2024_analysis.py
    │ └── merged_timeseries_analysis.py
    └── output/

### Step 4: Run Workflow

    snakemake --cores 1

Optional commands:
- Preview only: snakemake --cores 1 -n
- Force re-run: snakemake --cores 1 --forceall
- Use wrapper script: python run_pipeline.py

### Step 5: Outputs Generated in output/

PNG Figures (6 files):
- BankOwnership-Poverty2024Scatter.png
- MobileAccount-Poverty2024Scatter.png
- DigitalOwnership-Poverty2024Scatter.png
- DigitalAccess-Poverty2024Comparison.png
- TimeseriesGlobalTrendsPlot.png
- AveragedTimeseriesFinancialAccess-PovertyComparison.png

Data Outputs (2 files):
- correlation_analysis.csv
- regression_results.txt

Processed Data (6 files in data/processed/):
- pip_cleaned_2024.csv
- pip_cleaned_timeseries.csv
- findex_cleaned_2024.csv
- findex_cleaned_timeseries.csv
- master_dataset_2024.csv
- master_timeseries_dataset.csv


## References
- World Bank Global Findex Database
- World Bank Poverty and Inequality Platform
- Python Pandas Documentation
