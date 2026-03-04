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
INFO


# Constraints
INFO


# Gaps
INFO
