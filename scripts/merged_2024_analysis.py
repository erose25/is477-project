import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

file = "../processed/master_dataset_2024.csv"
df = pd.read_csv(file)

df = df.groupby('country_code')[["account_pct", "mobile_account_pct", "digital_account_pct", "poverty_headcount"]].mean()

cols = ["country_code", "account_pct", "mobile_account_pct", "digital_account_pct", "poverty_headcount"]

correlation = df[["account_pct", "mobile_account_pct", "digital_account_pct", "poverty_headcount"]].corr()
print(correlation)

plt.figure()
plt.scatter(df["account_pct"], df["poverty_headcount"])
plt.xlabel("Bank Account Ownership (%)")
plt.ylabel("Poverty Headcount (%)")
plt.title("Bank Account Ownership vs Poverty (2024)")
plt.savefig("../output/BankOwnership-Poverty2024Scatter.png")
plt.show()

plt.figure()
plt.scatter(df['mobile_account_pct'], df['poverty_headcount'])
plt.xlabel('Mobile Account Usage (%)')
plt.ylabel('Poverty Headcount (%)')
plt.title('Mobile Account vs Poverty (2024)')
plt.savefig("../output/MobileAccount-Poverty2024Scatter.png")
plt.show()

plt.figure()
plt.scatter(df['digital_account_pct'], df['poverty_headcount'])
plt.xlabel('Digitally-enabled Accounts (%)')
plt.ylabel('Poverty Headcount (%)')
plt.title('Digital Financial Inclusion vs Poverty (2024)')
plt.savefig("../output/DigitalOwnership-Poverty2024Scatter.png")
plt.show()

X = df[['account_pct', 'mobile_account_pct', 'digital_account_pct']]
y = df['poverty_headcount']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

best_cases = df.sort_values(['digital_account_pct', 'poverty_headcount'], ascending = [False, True]).head(2)
worst_cases = df.sort_values(['digital_account_pct', 'poverty_headcount'], ascending = [True, False]).head(2)

print("Best cases:\n", best_cases)
print("\nWorst cases:\n", worst_cases)

frames = [best_cases, worst_cases]
combined_best_worst = pd.concat(frames)
combined_best_worst.plot(kind = "bar")
plt.title("Digital Access & Poverty Comparison 2024")
plt.xlabel("Country")
plt.ylabel("Average Value")
plt.xticks(rotation = 45)
plt.legend(title = "Metrics")
plt.tight_layout()
plt.savefig("../output/DigitalAccess-Poverty2024Comparison.png")
plt.show()
