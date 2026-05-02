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
INFO

## Data Cleaning
INFO

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
INFO

## Challenges
INFO

## Reproducing
INFO

## References
- World Bank Global Findex Database
- World Bank Poverty and Inequality Platform
- Python Pandas Documentation
