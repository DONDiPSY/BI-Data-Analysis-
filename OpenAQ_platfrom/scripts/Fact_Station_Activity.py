import pandas as pd
from pathlib import Path

def build_fact_data(staging_path, fact_path, dim_tables):
    """
    Build the fact table by merging cleaned staging data with each
    dimension table, then assign a surrogate fact key.
    Parameters
    ----------
    staging_path : str or Path
        Path to the cleaned staging Parquet file.
    fact_path : str or Path
        Full output path (including filename) for the fact table Parquet file.
    dim_tables : dict[str, pd.DataFrame]
        Dimension tables keyed by name, e.g.
        {"dim_country": ..., "dim_owner": ..., "dim_provider": ..., "dim_station": ...}
    Returns
    -------
    fact_table : pd.DataFrame
        The fact table with a surrogate 'weather_id' plus each dimension's key.
    """
    fact_path = Path(fact_path)
    fact_df = pd.read_parquet(staging_path)
    # merging all dim to fact table
    fact_df= fact_df.merge(dim_tables["dim_country"], on="country_id", how="left")
    fact_df  = fact_df.merge(dim_tables["dim_owner"], on="owner_id", how="left")
    fact_df = fact_df.merge(dim_tables["dim_provider"], on="provider_id", how="left")
    fact_df = fact_df.merge(dim_tables["dim_instrument"], on="instrument_id", how="left")
    fact_df = fact_df.merge(dim_tables["dim_license"], on="license_id", how="left")
    # A surrogate key is created for dim_station , so the surrogate key can't be used to merge
    #  station_id directly — merge on the natural key columns instead
    fact_df = fact_df.merge(dim_tables["dim_station"], on=["name","locality", "timezone",
    "coordinates_latitude","coordinates_longitude", "isMobile","isMonitor"], how="left")


    # Adding a surrogate key
    fact_df["weather_id"]= fact_df.index + 40220
    fact_df["weather_id"] = fact_df["weather_id"].astype(int)
    fact_table = fact_df[["weather_id",
                      "country_id",
                      "owner_id",
                      "provider_id",
                      "instrument_id",
                      "license_id",
                      "sensor_id",
                      "first_measured_utc",
                        "last_measured_utc"
                      ]]
    print(fact_table.head(20))

    fact_path.parent.mkdir(parents=True, exist_ok=True)
    fact_table.to_parquet(fact_path, index=False, compression="snappy")

    print(f"input written data to {fact_path}, {len(fact_table)} rows")

    return fact_table


if __name__ == "__main__":
    from config import staging_dir, Fact_dir, Dimension_dir

    dim_tables = {
        "dim_country": pd.read_parquet(Dimension_dir / "Dim_country.parquet"),
        "dim_owner": pd.read_parquet(Dimension_dir / "Dim_owner.parquet"),
        "dim_provider": pd.read_parquet(Dimension_dir / "Dim_provider.parquet"),
        "dim_instrument": pd.read_parquet(Dimension_dir / "Dim_instrument.parquet"),
        "dim_license": pd.read_parquet(Dimension_dir / "Dim_license.parquet"),
        "dim_station": pd.read_parquet(Dimension_dir / "Dim_station.parquet")
    }
    staging_path = staging_dir/"ProcessedOpenAQ_platform.parquet"
    fact_path =  Fact_dir/"Fact_Activity.parquet"

    build_fact_data(staging_path, fact_path, dim_tables)


