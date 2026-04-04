import pandas as pd 

df = pd.read_csv("../raw/pip_dataset.csv")

df.head()
df.info()

## keeping only relevant rows to our analysis
df = df[[
    "country_code", 
    "country_name",
    "reporting_year",
    "headcount",
    "gini",
]]

## renaming for future merging 
df = df.rename(columns = {
    "reporting_year" : "year",
    "headcount" : "poverty_headcount"
})

## dropping the rows with unusual countries like "Sub-Saharan Africa" and "Europe and Central Asia"  
df = df[df["country_code"].notna()]
df = df[df["country_code"].str.len() == 3]

df.isnull().sum()

## removing duplicates where we have the same year more than once for the same country 
df = df.drop_duplicates(subset = ["country_code", "year"])

## ensuring correct data types 
df["year"] = df["year"].astype(int)
df["poverty_headcount"] = df["poverty_headcount"].astype(float)
df["gini"] = df["gini"].astype(float)

## sort for timeseries
df = df.sort_values(by = ["country_code", "year"])

## save cleaned dataset
df.to_csv("../processed/pip_cleaned.csv", index = False)
