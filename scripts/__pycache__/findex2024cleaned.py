import os
import pandas as pd

file = "C:/Users/harsh/Downloads/GlobalFindexDatabase2025.csv"
df = pd.read_csv(file)

df.columns = df.columns.str.strip().str.lower()
rename_map = {"countrynewwb": "country", "codewb": "country_code", "year": "year", "account_t_d": "account_pct", "fiaccount_t_d": "bank_account_pct", "mobileaccount_t_d": "mobile_account_pct", "borrow_any_t_d": "borrowed_pct", "save_any_t_d": "saved_pct", "dig_acc": "digital_account_pct"}

rename_map = {k: v for k, v in rename_map.items() if k in df.columns}
df = df.rename(columns = rename_map)

required_cols = ["country", "country_code", "year", "account_pct", "bank_account_pct", "mobile_account_pct", "digital_account_pct"]
existing_required = [col for col in required_cols if col in df.columns]
df = df[existing_required]

df = df[df["year"] == 2024]

df = df.dropna(subset = existing_required)

numeric_cols = ["account_pct", "bank_account_pct", "mobile_account_pct", "digital_account_pct"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors = "coerce")
df

output = "C:/Users/harsh/Downloads/findex_cleaned_2024.csv"
df.to_csv(output, index = False)
