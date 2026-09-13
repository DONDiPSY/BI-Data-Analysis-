import pandas as pd
import numpy as np
from config import Staging_Dir, Dim_Dir

staging_df = pd.read_parquet(Staging_Dir / "Processed_Payslim_mobile_money.parquet")
Dimension = Dim_Dir/"Dim_Fraud_Act.parquet"
df = staging_df.copy()
# keep only unique rows  combinations , reset the index to start cleanly from 0
dim_fraud = df[["isFraud", "isFlaggedFraud"]].drop_duplicates().reset_index(drop=True)

# creating a surrogate key : unique identifier
dim_fraud["fraud_id"] = dim_fraud.index + 10011


# assembling the dim table for fraud
dimen_Fraud = dim_fraud[["fraud_id","isFraud", "isFlaggedFraud"]]

dimen_Fraud.to_parquet(Dimension, index=False)

print(f"inputed written data to  {Dimension}, {len(dimen_Fraud)} rows")