import pandas as pd
import numpy as np
from config import Staging_Dir , Dim_Dir

staging_df = pd.read_parquet(Staging_Dir / "Processed_Payslim_mobile_money.parquet")
Dimension = Dim_Dir/"Dim_Type.parquet"
df = staging_df.copy()
#transaction Type dimension
dim_type = df[["type"]].drop_duplicates().reset_index(drop=True)
# surrogate key : unqiue identifier
dim_type["type_id"] = dim_type.index + 101

# merge back to main table


fact_df = df.drop(columns=["type"])

# assembling the transaction type
dimen_type = dim_type[["type_id", "type"]]

dimen_type.to_parquet(Dimension, index=False)

print(f"inputed written data to {Dimension}, {len(dimen_type)} rows")