import json
import pandas as pd
from pathlib import Path
def process_openaq_data(raw_json_path, staging_path):
    """
    Load a raw OpenAQ 'locations' JSON export, flatten the nested
    sensors / instruments / licenses / bounds fields into separate
    tables, clean up columns and datatypes, and write the cleaned
    parent (locations) table to a Parquet file.


    Parameters
    ----------
    raw_json_path : str or Path
        Path to the raw OpenAQ JSON file (e.g. "Raw_OpenAQ_....json").
    staging_dir : str or Path
        Full output path (including filename) for the cleaned Parquet file.


    Returns
    -------
    df : pd.DataFrame
        Cleaned locations (parent) table.
    sensor_df : pd.DataFrame
        One row per sensor. Links back to df via 'location_id'.
    df_instrument : pd.DataFrame
        One row per instrument. Links back to df via 'instrument_id'.
    license_df_data : pd.DataFrame
        One row per license. Links back to df via 'location_id'.
    """
    raw_json_path = Path(raw_json_path)
    staging_path = Path(staging_path)


    # 1. Load the JSON and turn the "results" list into a flat-ish DataFrame
    with open(raw_json_path) as f:
        data = json.load(f)
    df = pd.json_normalize(data["results"])

    # check if the 20 pages consist of actual columns  in page one
    expected_columns = {
        'id', 'name', 'locality', 'timezone', 'isMobile', 'isMonitor','distance', 'country.id',
        'country.code', 'country.name', 'owner.id', 'owner.name', 'provider.id', 'provider.name',
        'coordinates.latitude', 'coordinates.longitude', 'datetimeFirst.utc',
        'datetimeFirst.local', 'datetimeLast.utc', 'datetimeLast.local','bounds', 'sensors',
        'licenses', 'instruments', 'timezone'
    }
    actual_columns = set(df)
    new_cols = actual_columns.difference(expected_columns)
    missing_cols = expected_columns.difference(actual_columns)
    if new_cols:
        print(f"⚠️ New columns not in cleaning logic: {new_cols}")
    if missing_cols:
        print(f"⚠️ Expected columns missing from this pull: {missing_cols}")


    # 2. bounds is a 4-element list per row -> split it into 4 real columns
    df[["min_lon", "min_lat", "max_lon", "max_lax"]] = pd.DataFrame(
        df["bounds"].tolist(), index=df.index
    )
    df = df.drop(columns=["bounds"])


    # 3. sensors is a list of dicts per row -> explode so each sensor gets
    #    its own row, then flatten the dict into columns
    sensor_df = df[["id", "sensors"]].explode("sensors").reset_index(drop=True)
    sensor_df = sensor_df.rename(columns={"id": "location_id"})
    sensor_df = pd.concat(
        [sensor_df.drop(columns=["sensors"]), pd.json_normalize(sensor_df["sensors"])],
        axis=1,
    )
    sensor_df.columns = sensor_df.columns.str.replace(".", "_", regex=False)
    sensor_df = sensor_df.rename(columns={"id": "sensors_id"})
    df = df.drop(columns="sensors")


    # 4. licenses is a list of dicts (sometimes empty) -> explode, drop the
    #    empty rows, then flatten the dict into columns
    license_df_data = df[["id", "licenses"]].explode("licenses").reset_index(drop=True)
    license_df_data = license_df_data.rename(columns={"id": "location_id"})
    license_df_data = license_df_data[license_df_data["licenses"].notna()].reset_index(drop=True)
    license_df_data = pd.concat(
        [license_df_data.drop(columns=["licenses"]), pd.json_normalize(license_df_data["licenses"])],
        axis=1,
    )
    license_df_data = license_df_data.rename(columns={"id": "license_id"})


    # 5. instruments is a list of dicts per row -> same explode + flatten pattern
    df_instrument = df[["id", "instruments"]].explode("instruments").reset_index(drop=True)
    df_instrument = df_instrument.rename(columns={"id": "instrument_id"})
    df_instrument = pd.concat(
        [df_instrument.drop(columns=["instruments"]), pd.json_normalize(df_instrument["instruments"])],
        axis=1,
    )


    # instruments/licenses have now been split out into their own tables,
    # so drop the original nested columns from the parent table
    df = df.drop(columns=["instruments", "licenses"])


    # 6. tidy column names produced by json_normalize (e.g. "coordinates.latitude"
    #    -> "coordinates_latitude")
    df.columns = df.columns.str.replace(".", "_", regex=False)


    # 7. parse the timestamp columns as real datetimes instead of strings
    date_cols = ["datetimeFirst_utc", "datetimeFirst_local", "datetimeLast_utc", "datetimeLast_local"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce", utc=True)


    # "distance" is null for every row, and the un-split datetimeFirst/datetimeLast
    # dict columns are no longer needed now that *_utc/*_local exist
    df = df.drop(columns=["datetimeFirst", "datetimeLast", "distance"])


    # 8. min_lat/max_lax and min_lon/max_lon were found to be identical in every
    #    row, so keep only one of each pair and give them clear names
    df = df.drop(columns=["min_lat", "max_lon"])
    df = df.rename(columns={"min_lon": "longitude", "max_lax": "latitude"})


    # 9. fill missing locality with a readable placeholder
    df = df.fillna({"locality": "Unknown"})


    # 10. a handful of rows have no timestamp data at all - drop them
    ts_cols = ["datetimeFirst_utc", "datetimeLast_utc", "datetimeFirst_local", "datetimeLast_local"]
    df = df.dropna(subset=ts_cols)


    # 11. the bounds-derived latitude/longitude turned out to be identical to
    #     coordinates_latitude/coordinates_longitude - drop the redundant pair
    df = df.drop(columns=["latitude", "longitude"])


    # 12. write the cleaned parent table out as Parquet
    staging_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(staging_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {staging_path}, {len(df)} rows")


    return df, sensor_df, df_instrument, license_df_data

if __name__ == "__main__":
    from config import Raw_dir

    staging_dir = Raw_dir/ "stagingOpenAQ_platform" / "ProcessedOpenAQ_platform.parquet"
    process_openaq_data(raw_json_path= Raw_dir, staging_path =staging_dir,)

    # question
    # since this is working with an airflow how will get the access of filename name
    # after extracting  to reference the function process_openaq_data with the argument raw_json_path
"""
So instead of hardcoding "../Raw_OpenAQ_20260803_170745.json" like in your __main__ block,
your extract task should return the path it wrote to, and your staging task should receive 
it as a parameter:
"""