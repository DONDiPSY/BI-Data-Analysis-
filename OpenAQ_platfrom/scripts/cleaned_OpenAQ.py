import json
import pandas as pd
import numpy as np
from pathlib import Path
def process_openaq_data(raw_json_path, staging_path):

    """

    :param raw_json_path:
    :param staging_path:
    :return:  df
    Load file  into variable data
    using dictionary comprehension to return a unique id
    """

    raw_json_path = Path(raw_json_path)
    print(raw_json_path)
    print(raw_json_path.is_dir())
    staging_path = Path(staging_path)


    # 1. Load the JSON and turn the data  list into a flat-ish DataFrame
    with open(raw_json_path, encoding="utf-8") as f:
        data = json.load(f)

    # 1. Pages can Overlap --> Keep one record per location
    # dictionary comprehension key: value for item in iterable
    data = list({loc["id"]: loc for loc in data}.values())
    # confused
    # 2. Confirm that bounds equal the station point. If they don’t,
    # tell me instead of silently dropping those locations
    non_point = [i["id"] for i in data if not i.get("bounds") or not np.allclose(i["bounds"],
                [i["coordinates"]["longitude"],i["coordinates"]["latitude"]] * 2)]
    if non_point:
        print(f"⚠️ bounds differ from the point for locations: {non_point}")

    # 3. child tables : loop over dict so the parent id rides along
    sensors, instruments , licenses = [], [], []
    for loc in data:
        lid = loc["id"]
        for s in loc.get("sensors") or [] :
            p = s.get("parameter") or {}
            sensors.append({"sensor_id":s["id"], "location_id":lid,
                            "parameter_id": p.get("id"), "parameter_name": p.get("name"),
                            "units" : p.get("units"), "display_name":p.get("displayName")
                            })
        for i in loc.get("instruments") or []:
            instruments.append({"instrument_id":i["id"], "location_id":lid,
                                "instrument_name": i["name"]})
        for lic in loc.get("licenses") or []:
            licenses.append({"location_id":lid, "license_id": lic["id"],
                             "license_name": lic["name"],
                             "date_from":lic.get("dateFrom"), "date_to":lic.get("dateTo")})

    sensors_df = pd.DataFrame(sensors)
    instruments_df = pd.DataFrame(instruments)
    licenses_df = pd.DataFrame(licenses)

    # drop parent tables
    df = pd.json_normalize(data).drop(columns=["sensors", "instruments", "licenses", "bounds", "distance","datetimeFirst", "datetimeLast",
                 "datetimeFirst.local", "datetimeLast.local"], errors="ignore")
    # rename columns with "." to "_"
    df = df.rename(columns={
        "id": "location_id", "name": "location_name",
        "country.id": "country_id", "country.code": "country_code", "country.name": "country_name",
        "owner.id": "owner_id", "owner.name": "owner_name",
        "provider.id": "provider_id", "provider.name": "provider_name",
        "coordinates.latitude": "latitude", "coordinates.longitude": "longitude",
        "datetimeFirst.utc": "first_measured_utc", "datetimeLast.utc": "last_measured_utc",
        "isMobile": "is_mobile", "isMonitor": "is_monitor"})
   # remove white space in fields
    df = pd.concat([sensors_df, df], ignore_index=True)
    df = pd.concat([instruments_df, df], ignore_index=True)
    df = pd.concat([ licenses_df, df], ignore_index=True)
    df["location_name"] = df["location_name"].str.strip()
    loc = df["locality"].str.strip()
    df["locality"] = loc.mask(loc.isin(["","N/A"])).fillna("Unknown")
    df[["latitude", "longitude"]] = df[["latitude", "longitude"]].round(6)
    for c in ["first_measured_utc", "last_measured_utc"]:
        df[c] =pd.to_datetime(df[c], utc=True, errors="coerce")
        # issues

        # Create the raw data directory if it doesn't already exist
    staging_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(staging_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {staging_path}, {len(df)} rows")
    print(df.columns)
    return df


if __name__ == "__main__":
    from config import Raw_dir
    raw_json_dir = Raw_dir/"Raw_OpenAQ_20261004_142907.json"
    staging_dir = Raw_dir/ "stagingOpenAQ_platform" / "ProcessedOpenAQ_platform.parquet"
    process_openaq_data(raw_json_path=  raw_json_dir, staging_path =staging_dir)
