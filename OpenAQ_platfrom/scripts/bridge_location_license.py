import pandas as pd
from pathlib import Path
def  build_bridge_loc_license_data(staging_path, dim_path ,bridge_path):
    """

    :param staging_path:
    :param bridge_path:
    :return:
    Note A bridge table connects records when a many-to-many relationship
    exists. For example, if one location can have several license and
    the same license can be associated with multiple locations,
    a bridge table can represent those relationships
    """
    bridge_path = Path(bridge_path)
    df = pd.read_parquet(staging_path)
    dim_location = pd.read_parquet(dim_path["location"])
    dim_license = pd.read_parquet(dim_path["license"])
    bridge_license = df[["location_id", "license_id"]].drop_duplicates().reset_index(drop=True)
    bridge_license = bridge_license.merge(dim_location[["location_id","location_key"]], on="location_id", how="left")
    bridge_license =bridge_license.merge(dim_license[["license_key", "license_id"]], on="license_id", how="left")
    bridge_license = (bridge_license[["license_key", "location_key"]])


    bridge_path.parent.mkdir(parents=True, exist_ok=True)
    bridge_license.to_parquet(bridge_path,  engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {bridge_path}, {len(bridge_license)} rows")
    return bridge_license


if __name__ == "__main__":
    from config import staging_dir,Dimension_dir, Bridge_dir
    staging_path = staging_dir / "processed_licenseOpenAQ_platform.parquet"
    dim_path = {
        "location": Dimension_dir / "Dim_location.parquet",
        "license" : Dimension_dir / "Dim_license.parquet"
                }
    bridge_path = Bridge_dir / "Bridge_location_license.parquet"
    build_bridge_loc_license_data(staging_path, dim_path, bridge_path)
