#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().run_cell_magic('writefile', '../scripts/pip2024cleaning.py', '\nimport pandas as pd \n')


# In[13]:


df = pd.read_csv("../raw/pip_dataset.csv")

df.head()
df.info()


# In[14]:


## keeping only relevant rows to our analysis

df = df[[
    "country_code", 
    "country_name",
    "reporting_year",
    "headcount",
    "gini",
]]


# In[15]:


## renaming for future merging 

df = df.rename(columns = {
    "reporting_year" : "year",
    "headcount" : "poverty_headcount"
})


# In[16]:


## dropping the rows with unusual countries like "Sub-Saharan Africa" and "Europe and Central Asia"  

df = df[df["country_code"].notna()]
df = df[df["country_code"].str.len() == 3]


# In[17]:


df.isnull().sum()


# In[18]:


## removing duplicates where we have the same year more than once for the same country 

df = df.drop_duplicates(subset = ["country_code", "year"])


# In[19]:


## ensuring correct data types 

df["year"] = df["year"].astype(int)
df["poverty_headcount"] = df["poverty_headcount"].astype(float)
df["gini"] = df["gini"].astype(float)

df.to_csv("../processed/pip_cleaned_2024.csv", index = False)


# In[20]:


## sort for timeseries

df = df.sort_values(by = ["country_code", "year"])


# In[21]:


## save cleaned dataset

df.to_csv("../processed/pip_cleaned_timeseries.csv", index = False)


# In[22]:


df


# In[ ]:




