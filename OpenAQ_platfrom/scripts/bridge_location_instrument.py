import pandas as pd
from pathlib import Path
def  build_bridge_loc_instrument_data(staging_path, bridge_path):
    """

    :param staging_path:
    :param bridge_path:
    :return:
    Note A bridge table connects records when a many-to-many relationship
    exists. For example, if one location can have several instruments and
    the same instrument can be associated with multiple locations,
    a bridge table can represent those relationships
    """
    bridge_path = Path(bridge_path)
    df = pd.read_parquet(staging_path)
    bridge_instrument = df[["instrument_id", "location_id"]].drop_duplicates().reset_index(drop=True)
    bridge_path.parent.mkdir(parents=True, exist_ok=True)
    bridge_instrument.to_parquet(bridge_path,  engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {bridge_path}, {len(bridge_instrument)} rows")
    return bridge_instrument


if __name__ == "__main__":
    from config import staging_dir, Bridge_dir
    staging_path = staging_dir / "ProcessedOpenAQ_platform.parquet"
    bridge_path = Bridge_dir / "Bridge_location_instrument.parquet"
    build_bridge_loc_instrument_data(staging_path, bridge_path)
