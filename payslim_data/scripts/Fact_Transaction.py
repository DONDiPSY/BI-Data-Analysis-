import pandas as pd
from config import Staging_Dir, Fact_Dir,Dim_Dir
import numpy  as np
staging_df = pd.read_parquet(Staging_Dir / "Processed_Payslim_mobile_money.parquet")
Fact = Fact_Dir / "fact_transactions.parquet"
fact_df = staging_df.copy()
dim_tables = {
    "dim_type": pd.read_parquet(Dim_Dir / "Dim_Type.parquet"),
    "dim_time": pd.read_parquet(Dim_Dir / "Dim_Time.parquet"),
    "dim_fraud": pd.read_parquet(Dim_Dir / "Dim_Fraud_Act.parquet"),
    "dim_account": pd.read_parquet(Dim_Dir / "Dim_Account.parquet")
}
# merging all dim to fact table
fact_df = fact_df.merge(dim_tables["dim_fraud"], on=["isFraud", "isFlaggedFraud"], how="left")
fact_df = fact_df.merge(dim_tables["dim_time"], on="step", how= "left")
fact_df = fact_df.merge(dim_tables["dim_type"], on="type", how= "left")


fact_df = fact_df.merge(dim_tables["dim_account"][["account_id", "account_id_sk"]],
              left_on="nameOrig", right_on="account_id", how="left")

fact_df = fact_df.rename(columns={"account_id_sk": "origin_account_sk"})
fact_df = fact_df.drop(columns=["account_id"])


# merge destination account
fact_df = fact_df.merge(
    dim_tables["dim_account"][["account_id", "account_id_sk"]],
    left_on="nameDest",
    right_on="account_id",
    how="left"
)

fact_df = fact_df.rename(columns={"account_id_sk": "dest_account_sk"})
fact_df = fact_df.drop(columns=["account_id"])

fact_df = fact_df.drop(columns=["isFraud", "isFlaggedFraud", "step","type"])


# assembling the fact table
Fact_table =fact_df[["transaction_id", "type_id","step_id", "fraud_id", "origin_account_sk",  "dest_account_sk","amount_log","amount"]]
# create the dir if it doesn't exist
Fact.parent.mkdir(parents=True, exist_ok=True)
Fact_table.to_parquet(Fact, index=False)

print(f"inputed written data to {Fact}, {len(Fact_table)} rows")



