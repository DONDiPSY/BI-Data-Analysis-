import  pandas as pd
import numpy as np
from config import Staging_Dir, Dim_Dir

staging_df = pd.read_parquet(Staging_Dir / "Processed_Payslim_mobile_money.parquet")
Dimension = Dim_Dir/"Dim_Time.parquet"
df = staging_df.copy()

# dim time
# keep only unqiue rows reset the index to start cleanly from 0
dim_time = df[["step"]].drop_duplicates().reset_index(drop=True)
# creating a surrogate key : unique identifier
dim_time["step_id"] = dim_time.index + 10001



# assembling the dim table  time
dimen_time = dim_time[["step_id",  "step"]].copy()
dimen_time["hour"] = dim_time["step"] % 24
dimen_time["day"] = dim_time["step"] // 24



dimen_time.to_parquet(Dimension, index=False)

print(f"inputed written data to {Dimension}, {len(dimen_time)} rows")