import pandas as pd
from pathlib import Path
def  build_bridge_loc_license_data(staging_path, bridge_path):
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
    bridge_license = df[["location_id","location_id", "license_id", "date_from", "date_to"]].drop_duplicates().reset_index(drop=True)
    bridge_path.parent.mkdir(parents=True, exist_ok=True)
    bridge_license.to_parquet(bridge_path,  engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {bridge_path}, {len(bridge_license)} rows")
    return bridge_license


if __name__ == "__main__":
    from config import staging_dir, Bridge_dir
    staging_path = staging_dir / "ProcessedOpenAQ_platform.parquet"
    bridge_path = Bridge_dir / "Bridge_location_license.parquet"
    build_bridge_loc_license_data(staging_path, bridge_path)
