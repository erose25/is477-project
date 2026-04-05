#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().run_cell_magic('writefile', '../../scripts/pip2024cleaning.py', '')


# In[ ]:


import pandas as pd 


# In[ ]:


df = pd.read_csv("../raw/pip_dataset.csv")

df.head()
df.info()


# In[ ]:


## keeping only relevant rows to our analysis

df = df[[
    "country_code", 
    "country_name",
    "reporting_year",
    "headcount",
    "gini",
]]


# In[ ]:


## renaming for future merging 

df = df.rename(columns = {
    "reporting_year" : "year",
    "headcount" : "poverty_headcount"
})


# In[ ]:


## dropping the rows with unusual countries like "Sub-Saharan Africa" and "Europe and Central Asia"  

df = df[df["country_code"].notna()]
df = df[df["country_code"].str.len() == 3]


# In[9]:


df.isnull().sum()


# In[10]:


## removing duplicates where we have the same year more than once for the same country 

df = df.drop_duplicates(subset = ["country_code", "year"])


# In[ ]:


## ensuring correct data types 

df["year"] = df["year"].astype(int)
df["poverty_headcount"] = df["poverty_headcount"].astype(float)
df["gini"] = df["gini"].astype(float)

df.to_csv("../processed/pip_cleaned_2024.csv", index = False)


# In[ ]:


## sort for timeseries

df = df.sort_values(by = ["country_code", "year"])

df_2024 = df[df["year"] == 2024]

print(df_2024)


# In[ ]:


## save cleaned dataset

df.to_csv("../processed/pip_cleaned_timeseries.csv", index = False)


# In[ ]:


df


# In[ ]:


get_ipython().system("jupyter nbconvert --to script pip_cleaned.ipynb --output-dir='../../scripts/' --output='pip2024cleaning'")

