import pandas as pd 

findex = pd.read_csv("findex_cleaned_timeseries.csv")
pip = pd.read_csv("pip_cleaned.csv")

## standardize column names 
findex.columns = findex.columns.str.lower().str.strip()
pip.columns = pip.columns.str.lower().str.strip()

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

## filter pip for only rows present in findex 
findex_years = findex["year"].unique()
pip_filtered = pip[pip["year"].isin(findex_years)]

print("\nYears in Findex:", sorted(findex_years))
print("Years after filtering PIP:", sorted(pip_filtered["year"].unique()))

## merge datasets
merged = pd.merge(
    findex,
    pip_filtered,
    on=["country_code", "year"],
    how="inner"
)

print("\nMerged dataset shape:", merged.shape)
merged.head()

## check merge 
missing_summary = merged.isnull().sum()
print("\nMissing values by column:\n", missing_summary)

# Duplicate country-year rows
duplicates = merged.duplicated(subset=["country_code", "year"]).sum()
print("\nDuplicate country-year rows:", duplicates)

## save merged dataset 
output_path = "../processed/master_dataset.csv"
merged.to_csv(output_path, index=False)

print(f"\nMaster dataset saved to: {output_path}")
