from pathlib import Path
import pandas as pd

def build_license_data(staging_path, dim_path):
    """
       Build the license dimension table from the cleaned OpenAQ staging data.


       Parameters
       ----------
       staging_path : str or Path
           Path to the cleaned staging Parquet file (the output of
           process_openaq_data).
       dim_path : str or Path
           Full output path (including filename) for the license dimension
           Parquet file.


       Returns
       -------
       dim_license : pd.DataFrame
           One row per unique license_id, with "name", "dataFrom","dataTo",
           and 'country_name'.
       """

    staging_data = Path(staging_path)
    df = pd.read_parquet(staging_data)
    # pull out the license related columns  and collapse to one row per license
    dim_license = df[["license_id", "license_name", "license_attribution_name", "license_attribution_url",
                      "license_dateFrom", "license_dateTo" ]].drop_duplicates(subset=["license_id"]).reset_index(drop=True)
    dim_license.insert(0,"license_key", dim_license.index +3300)
    dim_license["license_key"] = dim_license["license_key"].astype(int)
    for time in ["license_dateFrom", "license_dateTo"]:
        dim_license[time] = pd.to_datetime(dim_license[time], format="%Y-%m-%d", errors="coerce").dt.date


    # sanity check: if license_id really identifies one names, the number of
    # unique rows here should match the number of unique license_id values in
    # the staging data. assert stops execution immediately (with the given
    # message) if that's ever not true, which flags a data-quality problem
    # rather than silently writing a broken dimension table.
    assert len(dim_license) == df["license_id"].nunique(), "Mismatch — investigate duplicates further"

    print(dim_license.head())
    print(f"Total unique licenses : {len(dim_license)}")

    dim_path.parent.mkdir(parents=True, exist_ok=True)
    dim_license.to_parquet(dim_path,engine="pyarrow", index=False, compression="snappy")
    print(f"cleaned and processed data is written to {dim_path}, {len(dim_license)} rows ")

    return dim_license

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    staging_dir = staging_dir / "processed_licenseOpenAQ_platform.parquet"
    dim_path = Dimension_dir / "Dim_license.parquet"

    build_license_data(staging_dir, dim_path)