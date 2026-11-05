import pandas as pd
from pathlib import Path

def attach_key(df, dim, natural_key , surrogate_key, name):
  """Look up one dimension's surrogate key and check nothing  went wrong."""
  row_before = len(df)
  out = df.merge(dim[[natural_key, surrogate_key]],on =natural_key, how="left", validate="m:1")
  assert len(out) == row_before, f"{name} : row count changed "
  print(f"{name}: {out[surrogate_key].isna().sum()} rows with no match")
  return out


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


    staging_license = staging_path["processed_license"]
    staging_sensor = staging_path["processed_sensor"]


    #  Base table: one row per sensor.
    base = staging_sensor[["sensor_id", "location_id", "parameter_id","provider_id"]]

    Base =base.merge(staging_license[["location_id", "license_id", "country_id", "owner_id"]],
                     on="location_id", how= "left", validate="m:1")

    fact_df = Base
    for natural, surrogate , dim in[
        ("location_id", "location_key", "dim_location"),
        ("license_id", "license_key", "dim_license"),
        ("country_id", "country_key", "dim_country"),
        ("owner_id", "owner_key", "dim_owner"),
        ("provider_id", "provider_key", "dim_provider"),
        ("parameter_id", "parameter_key", "dim_parameter"),
        ("sensor_id", "sensor_key", "dim_sensor"),
    ]:
        fact_df =attach_key(fact_df, dim_tables[dim], natural, surrogate, dim)
    key_cols = ["location_key", "country_key", "owner_key", "provider_key",
                 "parameter_key", "license_key", "sensor_key"]
    fact_table = fact_df[key_cols].drop_duplicates().reset_index(drop=True)
    fact_table.insert(0, "weather_key", fact_table.index + 40220)
    fact_table["weather_key"] = fact_table["weather_key"].astype(int)
    # sanity checks
    assert not fact_table[key_cols].isna().any().any(), "Some rows have no dimension"


    fact_path.parent.mkdir(parents=True, exist_ok=True)
    fact_table.to_parquet(fact_path, index=False, compression="snappy")

    print(f"input written data to {fact_path}, {len(fact_table)} rows")

    return fact_table


if __name__ == "__main__":
    from config import staging_dir, Fact_dir, Dimension_dir

    dim_tables = {
        "dim_location": pd.read_parquet(Dimension_dir / "Dim_location.parquet"),
        "dim_country": pd.read_parquet(Dimension_dir / "Dim_country.parquet"),
        "dim_owner": pd.read_parquet(Dimension_dir / "Dim_owner.parquet"),
        "dim_provider": pd.read_parquet(Dimension_dir / "Dim_provider.parquet"),
        "dim_parameter": pd.read_parquet(Dimension_dir / "Dim_parameter.parquet"),
        "dim_license": pd.read_parquet(Dimension_dir / "Dim_license.parquet"),
        "dim_sensor": pd.read_parquet(Dimension_dir / "Dim_sensor.parquet")
    }

    staging_path = {
        "processed_license" : pd.read_parquet(staging_dir/"processed_licenseOpenAQ_platform.parquet"),
        "processed_sensor" : pd.read_parquet(staging_dir /"processed_sensorsOpenAQ_platform.parquet")

                    }

    fact_path =  Fact_dir/"Fact_Activity.parquet"

    build_fact_data(staging_path, fact_path, dim_tables)


"""
Removed Dimension Instrument from fact table due to many to many location on instrument 
there is a duplicate of  same location_id  on particular instrument 
created a bridge on that already 

"""