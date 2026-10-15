import pandas as pd
from pathlib import Path

# read the clean and processed parquet file
def build_sensor_data(staging_path, dim_sensor_path):
    dim_sensor_path = Path(dim_sensor_path)
    df = pd.read_parquet(staging_path)
    # keep only unique rows , combinations, reset the index to start cleanly from 0
    dim_sensor = df[["sensor_id","location_id","parameter_id", "parameter_name", "display_name","units"]].drop_duplicates("sensor_id").reset_index(drop=True)

    dim_sensor["sensors_for_same_parameter"] = (
    dim_sensor.groupby(["location_id", "parameter_id"])["sensor_id"]).transform("count")


    # curious why dim_sensor should have columns  and why bridge_
    # create a directory
    dim_sensor_path.parent.mkdir(parents=True, exist_ok=True)
    dim_sensor.to_parquet(dim_sensor_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {dim_sensor_path}, {len(dim_sensor)} rows")


    return dim_sensor

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    # location save the parquet file
    staging_path = staging_dir / "ProcessedOpenAQ_platform.parquet"
    dim_sensor_path = Dimension_dir/"Dim_sensor.parquet"
    build_sensor_data(staging_path, dim_sensor_path)

# Question location id is existing in staging df ,
# which can be used for dim_station instead  of creating a surrogate for dim station
# I noticed that in the cleaned_openAQ.py location_id exist twice in both variable sensor_df and license_df
# won't this cause redundancy  in star-schema  when I use location_id