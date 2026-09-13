import pandas as pd
from pathlib import Path

# read the clean and processed parquet file
def build_station_data(staging_path, dim_station_path):
    dim_station_path = Path(dim_station_path)
    df = pd.read_parquet(staging_path)
    # keep only unique rows , combinations, reset the index to start cleanly from 0
    dim_station = df[["name","locality", "timezone", "coordinates_latitude","coordinates_longitude", "isMobile","isMonitor"]].drop_duplicates().reset_index(drop=True)

    # create a surrogate key : Unique identifier
    dim_station["station_id"] = dim_station.index + 20040

    # selection re-order
    dim_station =dim_station[["station_id","name","locality", "timezone", "coordinates_latitude","coordinates_longitude", "isMobile","isMonitor"]]
    # create a directory
    dim_station_path.parent.mkdir(parents=True, exist_ok=True)
    dim_station.to_parquet(dim_station_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {dim_station_path}, {len(dim_station)} rows")


    return dim_station

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    # location save the parquet file
    staging_path = staging_dir / "ProcessedOpenAQ_platform.parquet"
    dim_station_path = Dimension_dir/"Dim_station.parquet"
    build_station_data(staging_path, dim_station_path)

# Question location id is existing in staging df ,
# which can be used for dim_station instead  of creating a surrogate for dim station
# I noticed that in the cleaned_openAQ.py location_id exist twice in both variable sensor_df and license_df
# won't this cause redundancy  in star-schema  when I use location_id