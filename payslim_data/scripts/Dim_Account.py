import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from config import Staging_Dir, Dim_Dir

staging_df = pd.read_parquet(Staging_Dir / "Processed_Payslim_mobile_money.parquet")
Dimension = Dim_Dir/"Dim_Account.parquet"
# separate memory for a back up space
df = staging_df.copy()
# dimension account
origin= df[["nameOrig"]].copy()
origin["account_type"] = "ORIGIN"
origin = origin.rename(columns= {"nameOrig":"account_id"})

dest = df[["nameDest"]].copy()
dest["account_type"] ="DESTINATION"
dest =dest.rename(columns={"nameDest":"account_id"})
# combine both table into one
dim_account = pd.concat([origin,dest], ignore_index=True)
#remove duplicate rows
dim_account = dim_account.drop_duplicates().reset_index(drop=True)
# creating a surrogate key : unique identifier
dim_account["account_id_sk"] = dim_account.index + 1001
#merge origin account

# assembling the dim table  account type
dimen_account =dim_account[["account_id", "account_id_sk", "account_type"]]
# creating a directory
Dimension.parent.mkdir(parents=True, exist_ok=True)
dimen_account.to_parquet(Dimension, index=False)
print(f"input written data to {Dimension}, {len(dimen_account)} rows")