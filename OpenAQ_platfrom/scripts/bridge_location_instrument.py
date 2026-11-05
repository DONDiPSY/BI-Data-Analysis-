import pandas as pd
from pathlib import Path

def build_loc_instrument_data(staging_path, dim_path, bridge_path):

    df = pd.read_parquet(staging_path)
    # read  dim - parquet file
    dim_location = pd.read_parquet(dim_path["location"])
    dim_instrument = pd.read_parquet(dim_path["instrument"])

    bridge_instrument = df[["instrument_id", "location_id"]].drop_duplicates().reset_index(drop=True)
    #  merge columns using location_id as a match dataframe
    bridge_instrument = bridge_instrument.merge(
        dim_location[["location_id","location_key"]],
            on="location_id", how="left")
    bridge_instrument = bridge_instrument.merge(
        dim_instrument[["instrument_id", "instrument_key"]],
        on="instrument_id", how="left")

    bridge_instrument = bridge_instrument[["instrument_key", "location_key"]].drop_duplicates().reset_index(drop=True)
    bridge_path.parent.mkdir(parents=True, exist_ok=True)
    bridge_instrument.to_parquet(bridge_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {bridge_path}, {len(bridge_instrument)} rows")
    return bridge_instrument

if __name__ == "__main__":
    from config import Dimension_dir, staging_dir, Bridge_dir
    staging_path = staging_dir /"processed_instrumentOpenAQ_platform.parquet"
    dim_path = {
        "location" : Dimension_dir / "Dim_location.parquet",
        "instrument" : Dimension_dir / "Dim_instrument.parquet"
    }
    bridge_path = Bridge_dir / "Bridge_location_instrument.parquet"

    build_loc_instrument_data(staging_path, dim_path, bridge_path)
