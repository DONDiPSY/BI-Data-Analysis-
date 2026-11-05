import pandas as pd
from pathlib import Path

from Dipsy.OpenAQ_platfrom.scripts.config import Dimension_dir
from Dipsy.payslim_data.scripts.config import Dim_Dir


def build_location_data(staging_path, dim_path ):
    """

    :param staging_path:
    :param dim_path:
    :return: dim location
    """

    dim_path = Path(dim_path)
    df = pd.read_parquet(staging_path)

    dim_location = df[["location_id", "location_name", "locality","timezone"
                       ,"latitude","longitude", "is_mobile", "is_monitor", "first_datetime_utc",
                       "last_datetime_utc"]].drop_duplicates(subset="location_id").reset_index(drop=True)
    dim_location.insert(0,"location_key",dim_location.index + 1000)
    dim_location["location_key"] = dim_location["location_key"].astype(int)

    # sanity check: if location_id really identifies one location_name , the number of
    # unique rows here should match the number of unique location_id values in
    # the staging data. assert stops execution immediately (with the given
    # message) if that's ever not true, which flags a data-quality problem
    # rather than silently writing a broken dimension table.
    assert len(dim_location) == dim_location["location_id"].nunique() , "Mismatch — investigate duplicates further"

    dim_path.parent.mkdir(parents=True, exist_ok=True)
    dim_location.to_parquet(dim_path, index=False, engine="pyarrow", compression="snappy")
    print(len(dim_location))
    return dim_location

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    staging_path = staging_dir/"processed_instrumentOpenAQ_platform.parquet"
    dim_path = Dimension_dir / "Dim_location.parquet"
    build_location_data(staging_path, dim_path)
