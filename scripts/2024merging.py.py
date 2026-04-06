#!/usr/bin/env python
# coding: utf-8

# In[48]:


get_ipython().run_cell_magic('writefile', '../../scripts/2024merging.py', '')


# In[55]:


import pandas as pd 


# In[56]:


findex = pd.read_csv("findex_cleaned_timeseries.csv")
pip = pd.read_csv("pip_cleaned_timeseries.csv")


# In[57]:


## standardize column names 

findex.columns = findex.columns.str.lower().str.strip()
pip.columns = pip.columns.str.lower().str.strip()


# In[58]:


## ensure key columns match 

if "countrycode" in findex.columns:
    findex = findex.rename(columns = {"countrycode" : "country_code"})

if "countrycode" in pip.columns:
    pip = pip.rename(columns = {"countrycode" : "country_code"})

if "year " in pip.columns:
    pip = pip.rename(columns = {"year " : "year"})

#check 
assert "country_code" in findex.columns, "country_code missing in findex"
assert "year" in findex.columns, "year missing in findex"
assert "country_code" in pip.columns, "country_code missing in pip"
assert "year" in pip.columns, "year missing in pip"


# In[59]:


## filter pip for only rows present in findex 
findex_years = findex["year"].unique()
pip_filtered = pip[pip["year"].isin(findex_years)]

print("\nYears in Findex:", sorted(findex_years))
print("Years after filtering PIP:", sorted(pip_filtered["year"].unique()))


# In[60]:


## merge datasets
merged = pd.merge(
    findex,
    pip_filtered,
    on=["country_code", "year"],
    how="inner"
)

print("\nMerged dataset shape:", merged.shape)
merged.head()


# In[61]:


## check merge 
missing_summary = merged.isnull().sum()
print("\nMissing values by column:\n", missing_summary)

# Duplicate country-year rows
duplicates = merged.duplicated(subset=["country_code", "year"]).sum()
print("\nDuplicate country-year rows:", duplicates)


# In[62]:


## save merged dataset 
output_path = "../processed/master_timeseries_dataset.csv"
merged.to_csv(output_path, index=False)

print(f"\nMaster dataset saved to: {output_path}")


# In[67]:


findex_2024 = pd.read_csv("findex_cleaned_2024.csv")
pip_2024 = pd.read_csv("pip_cleaned_2024.csv")


# In[68]:


## standardize column names 
findex_2024.columns = findex_2024.columns.str.lower().str.strip()
pip_2024.columns = pip_2024.columns.str.lower().str.strip()


# In[69]:


## ensure key columns match 

if "countrycode" in findex_2024.columns:
    findex_2024 = findex_2024.rename(columns = {"countrycode" : "country_code"})

if "countrycode" in pip_2024.columns:
    pip_2024 = pip_2024.rename(columns = {"countrycode" : "country_code"})

if "year " in pip_2024.columns:
    pip_2024 = pip_2024.rename(columns = {"year " : "year"})


# In[70]:


#check 
assert "country_code" in findex_2024.columns, "country_code missing in findex"
assert "year" in findex_2024.columns, "year missing in findex"
assert "country_code" in pip_2024.columns, "country_code missing in pip"
assert "year" in pip_2024.columns, "year missing in pip"


# In[73]:


## filter pip for only rows present in findex 
findex_years_2024 = findex_2024["year"].unique()
pip_filtered_2024 = pip_2024[pip_2024["year"].isin(findex_years)]

print("\nYears in Findex:", sorted(findex_years_2024))
print("Years after filtering PIP:", sorted(pip_filtered_2024["year"].unique()))


# In[74]:


## merge datasets
merged_2024 = pd.merge(
    findex_2024,
    pip_2024,
    on=["country_code", "year"],
    how="inner"
)

print("\nMerged dataset shape:", merged_2024.shape)
merged_2024.head()


# In[75]:


## check merge 
missing_summary = merged_2024.isnull().sum()
print("\nMissing values by column:\n", missing_summary)

# Duplicate country-year rows
duplicates = merged_2024.duplicated(subset=["country_code", "year"]).sum()
print("\nDuplicate country-year rows:", duplicates)


# In[76]:


## save merged dataset 
output_path_2024 = "../processed/master_dataset_2024.csv"
merged.to_csv(output_path_2024, index=False)

print(f"\nMaster dataset saved to: {output_path}")


# In[77]:


get_ipython().system("jupyter nbconvert --to script merging.ipynb --output-dir='../../scripts/' --output='2024merging.py'")


# In[ ]:




