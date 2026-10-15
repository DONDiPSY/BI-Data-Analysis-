from pathlib import Path
import pandas as pd



def build_instrument_data(staging_path, dim_path):
    """
           Build the instrument dimension table from the cleaned OpenAQ staging data.


           Parameters
           ----------
           staging_path : str or Path
               Path to the cleaned staging Parquet file (the output of
               process_openaq_data).
           dim_path : str or Path
               Full output path (including filename) for the instrument dimension
               Parquet file.


           Returns
           -------
           dim_instrument : pd.DataFrame
               One row per unique instrument_id, with "name"
               and 'country_name'.
           """


    staging_path = Path(staging_path)
    df = pd.read_parquet(staging_path)
    # pull out the instrument_id and name
    print(df.columns)
    dim_instrument = df[["instrument_id","location_id", "instrument_name"]].drop_duplicates(["location_id", "instrument_id"]).reset_index(drop=True)
    dim_instrument = dim_instrument[["instrument_id","instrument_name"]].drop_duplicates()
    # sanity check: if instrument_id really identifies one names, the number of
    # unique rows here should match the number of unique instrument_id values in
    # the staging data. assert stops execution immediately (with the given
    # message) if that's ever not true, which flags a data-quality problem
    # rather than silently writing a broken dimension table
    assert len(dim_instrument) == df["instrument_id"].nunique(), "Mismatch - investigate duplicates further"

    print(dim_instrument)
    print(f"Total unique instrument ids: {len(dim_instrument)}")

    dim_path.parent.mkdir(parents=True, exist_ok=True)
    dim_instrument.to_parquet(dim_path, engine="pyarrow", index=False , compression="snappy")
    print(f"Clean and stored instrument dimension table in Parquet file: {dim_path}, {len(dim_instrument)} rows")

    return dim_instrument


if __name__ == "__main__":
    from config import staging_dir, Dimension_dir

    staging_path = staging_dir/"ProcessedOpenAQ_platform.parquet"
    dim_path = Dimension_dir / "Dim_instrument.parquet"

build_instrument_data(staging_path, dim_path)