import sys
import pandas as pd
import numpy as np
from config import Staging_Dir, Base_Dir
Raw_path = Base_Dir /"payslim_raw_data"/"PS_20174392719_1491204439457_log.csv"
# directory to save file
staging_paysim= Base_Dir /"staging_paysim"/"Processed_Payslim_mobile_money.parquet"

df = pd.read_csv(Raw_path)
df.info()
# no missing value
print(df.isnull().sum())

# no duplicated rows
print(df.describe())
# back_up of dataset
back_up_df = df.copy()

print(df[df["amount"] == 0])
print(df.nlargest(10, "amount"))

# this code check for imbalance in the column isfraud
# calculate the percentage distribution of fraud vs non-Fraud
# value_counts() how may times each values appears
# normalize=True instead of raw count it returns proportion
#  convert to percentage of the proportion
print(df["isFraud"].value_counts(normalize=True) * 100)

# This line create a cross-tabulation (contingency table)
# it show how two columns relate to each other simultaneously
# together
print(pd.crosstab(df["isFraud"], df["isFlaggedFraud"]))
print(df[["isFraud", "isFlaggedFraud"]].isnull().sum())

print(df["type"].nunique())

print(df.duplicated().sum())
# create a function to change data type for the type column,
#  solve outliers for amount by creating a column amount_log
#create a unique transaction_id starting from 100 using the dataframe index
def datatype(df):
    df["type"] = df["type"].astype("category")
    df["amount_log"] = np.log1p(df["amount"])
    df["transaction_id"] = df.index + 100

    return df

df = datatype(df)

staging_paysim.parent.mkdir(parents=True, exist_ok=True)

# 3. Write the cleaned result into staging
df.to_parquet(staging_paysim, index=False)

print(f"Cleaned data written to {staging_paysim}, {len(df)} rows")
