import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

file = "../processed/master_timeseries_dataset.csv"
df = pd.read_csv(file)

df["Account_Change"] = df.groupby("country_code")["account_pct"].diff()
df["Mobile_Change"] = df.groupby("country_code")["mobile_account_pct"].diff()
df["Poverty_Change"] = df.groupby("country_code")["poverty_headcount"].diff()

correlation = df[["account_pct", "mobile_account_pct", "poverty_headcount"]].corr()
print(correlation)

reg_df = df.dropna()
X = reg_df[["account_pct", "mobile_account_pct"]]
y = reg_df["poverty_headcount"]
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

global_trends = df.groupby("year")[["account_pct", "mobile_account_pct", "poverty_headcount"]].mean()
print(global_trends)

cols = ["account_pct", "mobile_account_pct", "poverty_headcount"]
countries = ["ZWE", "TGO", "NER", "MYS", "RUS", "ZAF"]

import matplotlib.pyplot as plt
global_trends.plot(linewidth = 3)
plt.title("Global Trends: Financial Inclusion vs Poverty")
plt.xlabel("Year")
plt.ylabel("Value")
plt.savefig("../output/TimeseriesGlobalTrendsPlot.png")
plt.show()

country_avg_df = (df.groupby("country_code")[cols].mean().loc[countries])

country_avg_df.plot(kind = "bar")
plt.title("Financial Access & Poverty Comparison by Country")
plt.xlabel("Country")
plt.ylabel("Average Value")
plt.xticks(rotation = 45)
plt.legend(title = "Metrics")
plt.tight_layout()
plt.savefig("../output/AveragedTimeseriesFinancialAccess-PovertyComparison.png")
plt.show()
