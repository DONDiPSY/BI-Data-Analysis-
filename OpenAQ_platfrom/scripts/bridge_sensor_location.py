import pandas as pd
from pathlib import Path



def  build_bridge_loc_sensor_data(staging_path, dim_path,  bridge_path):
    """
    Running this code show the same rows as dim_sensor :
     which give a conclusion of one to one mapping
    :param staging_path:
    :param bridge_path:
    :return:
    Note A bridge table connects records when a many-to-many relationship
    exists. For example, if one location can have several sensor and
    the same sensor can be associated with multiple locations,
    a bridge table can represent those relationships
    """
    bridge_path = Path(bridge_path)
    dim_location = pd.read_parquet(dim_path["location"])
    dim_sensor = pd.read_parquet(dim_path["sensor"])
    df = pd.read_parquet(staging_path)
    bridge_sensor = df[["location_id", "sensor_id"]].drop_duplicates().reset_index(drop=True)



    bridge_sensor = bridge_sensor.merge(
        dim_location[["location_id", "location_key"]],
        on="location_id",
        how="left"
    )
    bridge_sensor = bridge_sensor.merge(
        dim_sensor[["sensor_id", "sensor_key"]],
        on="sensor_id",
        how="left"
    )
    bridge_sensor = (bridge_sensor[["location_key", "sensor_key"]].drop_duplicates().reset_index(drop=True))
    bridge_path.parent.mkdir(parents=True, exist_ok=True)
    bridge_sensor.to_parquet(bridge_path,  engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {bridge_path}, {len(bridge_sensor)} rows")
    return bridge_sensor


if __name__ == "__main__":
    from config import staging_dir, Dimension_dir, Bridge_dir
    staging_path = staging_dir/ "processed_sensorsOpenAQ_platform.parquet"
    dim_path = {
        "sensor":Dimension_dir / "Dim_sensor.parquet",
        "location": Dimension_dir / "Dim_location.parquet"}
    bridge_path = Bridge_dir / "Bridge_location_sensor.parquet"
    build_bridge_loc_sensor_data(staging_path,dim_path, bridge_path)


# I need to create a surrogate key from my staging file
# so I can achieve a bridge where both are common
# i solve the comment by creating a surrogate key on each dimension


