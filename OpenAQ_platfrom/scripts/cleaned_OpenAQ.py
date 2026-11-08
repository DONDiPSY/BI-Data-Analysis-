import json
import os
import pandas as pd
import numpy as np
from pathlib import Path



def process_openaq_data(raw_json_path, staging_path):
    # 1. Load the raw JSON
    with open(raw_json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        # Check that the JSON has the expected structure
    if not isinstance(data, list):
        raise ValueError("No Expected a list of OpenAQ_location records.")

    # understanding the shape of your data
    print(type(data))
    print(len(data))
    print(data[0].keys())
    print(f"bounds : {data[0]['bounds'][0:4]}")
    print(f"Parameter : {data[0]['sensors'][0]['parameter']}")
    print(f"Sensor: {data[0]['sensors']}")
    print(f"coordinates: {data[0]['coordinates']}")
    print(f"country: {data[0]['country']}")
    print(f"instrument:{data[0]['instruments']}")


    # 2. Flatten nested location-level dictionaries
    df = pd.json_normalize(data, sep="_")

    #understanding missing values
    print("\nMissing values: ")
    print(df.isna().sum().sort_values(ascending=False))
    # checking data types
    print("\nData type : ")
    print(df.dtypes)

    #understanding Duplicate and missing Location IDs
    print("\nDuplicate location IDs: ")
    print(df["id"].duplicated().sum())
    print("\nMissing location IDs: ")
    print(df["id"].isna().sum())
    # understanding missing blank name
    print("\nMissing  names: ")
    name = df["name"].astype("string").str.strip()
    print((name.isna() | name.eq("")).sum())

    # 3. Rename columns to consistent names
    df = df.rename(columns={
        "id": "location_id",
        "name": "location_name",
        "isMobile": "is_mobile",
        "isMonitor": "is_monitor",
        "coordinates_latitude": "latitude",
        "coordinates_longitude": "longitude",
        "country_id": "country_id",
        "country_code": "country_code",
        "country_name": "country_name",
        "owner_id": "owner_id",
        "owner_name": "owner_name",
        "provider_id": "provider_id",
        "provider_name": "provider_name",
        "datetimeFirst_utc": "first_datetime_utc",
        "datetimeLast_utc": "last_datetime_utc",
        "datetimeFirst_local": "first_datetime_local",
        "datetimeLast_local": "last_datetime_local",
    })

    # 4. Clean text columns
    for col in ["location_name", "locality", "timezone",
                "country_name", "owner_name", "provider_name"]:
        if col in df.columns:
            df[col] = df[col].replace(r"^\s*$", pd.NA, regex=True)
    data_columns = ["first_datetime_utc", "last_datetime_utc"]
    for col in data_columns:
        print(f"\n ---{col}---")
        print("Data types: ", df[col].dtype )
        print("Empty strings", df[col].astype("string").str.strip().eq("").sum())
        print("Unique sample values:")
        print(df[col].dropna().astype(str).unique()[:10])
        print("Missing values: ", df[col].isnull().sum())
        print(df[col].dropna().head(10).tolist())
        print("values types:", df[col].dropna().map(type).value_counts())

    for col in data_columns:
        df[col] = df[col]

        df[col] = pd.to_datetime(
            df[col],
            format="ISO8601",
            errors="coerce",
            utc=True
        )




    # Use Unknown for missing locality, not for every missing field
    df["locality"] = df["locality"].fillna("Unknown")

    # 5. Drop rows with missing values
    df = df.dropna(subset=["location_id", "location_name"])

    # Location IDs should identify one location
    df = df.drop_duplicates(subset=["location_id"], keep="first")
    print(df.dtypes)

    # 6. Extract sensors nested  from each original location record(Explode list)
    sensor_records = []
    instrument_record = []
    license_record = []

    for loc in data:
        location_id = loc.get("id")
        # Extract sensors
        for sensor in loc.get("sensors") or []:
            if not isinstance(sensor, dict):
                continue
            parameter = sensor.get("parameter") or {}

            sensor_records.append({
                "location_id": location_id,
                "sensor_id": sensor.get("id"),
                "sensor_name": sensor.get("name"),
                "parameter_id": parameter.get("id"),
                "parameter_name": parameter.get("name"),
                "parameter_units": parameter.get("units"),
                "parameter_display_name": parameter.get("displayName"),
            })
            # Extract licenses
        for license in loc.get("licenses") or []:
            if not isinstance(license, dict):
                continue
            Attribution=license.get("attribution") or {}
            license_record.append({
            "location_id": location_id,
            "license_id": license.get("id"),
            "license_name" : license.get("name"),
            "license_attribution_name":Attribution.get("name"),
                    "license_attribution_url" :Attribution.get("url"),
                    "license_dateFrom" :license.get("dateFrom"),
                    "license_dateTo" : license.get("dateTo")})
                # Extract instruments
        for instrument in loc.get("instruments") or []:
            if not  isinstance(instrument, dict):
                continue
            instrument_record.append({
                "location_id": location_id,
                "instrument_id": instrument.get("id"),
                 "instrument_name" : instrument.get("name")
                    })


    sensors_df = pd.DataFrame(sensor_records)
    license_df = pd.DataFrame(license_record)
    instrument_df =pd.DataFrame(instrument_record)
    # 7. Clean sensor records
    if not sensors_df.empty:
        sensors_df = sensors_df.dropna(
            subset=["location_id", "sensor_id"]
        )

        sensors_df = sensors_df.drop_duplicates(
            subset=["location_id", "sensor_id"]
        )

    # Clean license records
    if not license_df.empty:
        license_df = license_df.dropna(
            subset=["location_id", "license_id"]
        )

        license_df = license_df.drop_duplicates(
            subset=["location_id", "license_id"]
        )

    # Clean instrument records
    if not instrument_df.empty:
        instrument_df = instrument_df.dropna(
            subset=["location_id", "instrument_id"]
        )

        instrument_df = instrument_df.drop_duplicates(
            subset=["location_id", "instrument_id"]
        )

    # 8. Join clean location attributes to the sensor records
    location_columns = [
        "location_id", "location_name", "locality", "timezone",
        "country_id", "country_code", "country_name",
        "owner_id", "owner_name", "provider_id", "provider_name",
        "latitude", "longitude", "is_mobile", "is_monitor",
        "first_datetime_utc", "last_datetime_utc"
    ]

    location_columns = [
        col for col in location_columns if col in df.columns
    ]
    print("LOCATION DATA")
    for col in data_columns:
        print(col, df[col].isnull().sum())
    print("\n SENSOR DATA")
    print(f"sensor row: {len(sensors_df)}")
    print(f"Unqiue location: {sensors_df['location_id'].nunique()}")

    sensor_staging_df = sensors_df.merge(
        df[location_columns],
        on="location_id",
        how="left",
        validate="many_to_one"
    )
    # Merge licenses with location attributes
    license_staging_df = license_df.merge(
        df[location_columns],
        on="location_id",
        how="left",
        validate="many_to_one")

    # Merge instruments with location attributes
    instrument_staging_df = instrument_df.merge(
        df[location_columns],
        on="location_id",
        how="left",
        validate="many_to_one"
    )
    # 9. Validate the output
    relationships = {
        "Sensors": (sensor_staging_df, ["location_id", "sensor_id"]),
        "Licenses": (license_staging_df, ["location_id", "license_id"]),
        "Instruments": (instrument_staging_df, ["location_id", "instrument_id"])
    }

    for name, (staging_df, keys) in relationships.items():

        if staging_df.duplicated(subset=keys).any():
            raise ValueError(f"Duplicate {name} relationships found.")

        if staging_df["location_id"].isna().any():
            raise ValueError(f"Missing location IDs in {name} staging data.")

    # 10. Save the staging file



    for name, path in staging_path.items():
        S_path = Path(path)
        S_path.parent.mkdir(parents=True, exist_ok=True)

        if name == "processed_sensor":
            output_df = sensor_staging_df

        elif name == "processed_license":
            output_df = license_staging_df

        elif name == "processed_instrument":
            output_df = instrument_staging_df

        else:
            raise ValueError(f"Unknown staging file: {name}")

        output_df.to_parquet(
            S_path,
            engine="pyarrow",
            index=False,
            compression="snappy"
        )

        print(f"Saved {name}: {S_path}")
    print(sensor_staging_df.isna().sum().sort_values(ascending=False))
    print(license_staging_df.isna().sum().sort_values(ascending=False))
    print(instrument_staging_df.isna().sum().sort_values(ascending=False))
    print(instrument_staging_df.columns)
    print(license_staging_df.columns)
    print(sensor_staging_df.columns)
    return  sensor_staging_df, license_staging_df, instrument_staging_df




if __name__ == "__main__":
    from config import Raw_dir
    raw_json_dir = Raw_dir/"Raw_OpenAQ_20261004_142907.json"
    staging_dir = {"processed_sensor" : Raw_dir/ "stagingOpenAQ_platform" / "processed_sensorsOpenAQ_platform.parquet",
                   "processed_license" : Raw_dir/ "stagingOpenAQ_platform" / "processed_licenseOpenAQ_platform.parquet",
                   "processed_instrument":Raw_dir/ "stagingOpenAQ_platform" / "processed_instrumentOpenAQ_platform.parquet" }


    process_openaq_data(raw_json_path=  raw_json_dir, staging_path = staging_dir)
