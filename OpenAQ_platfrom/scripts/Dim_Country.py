import pandas as pd
from pathlib import Path


def build_country_data(staging_path, dim_path):
    """
    Build the country dimension table from the cleaned OpenAQ staging data.


    Parameters
    ----------
    staging_path : str or Path
        Path to the cleaned staging Parquet file (the output of
        process_openaq_data).
    dim_path : str or Path
        Full output path (including filename) for the country dimension
        Parquet file.


    Returns
    -------
    dim_country : pd.DataFrame
        One row per unique country, with 'country_id', 'country_code',
        and 'country_name'.
    """

    dim_path =Path(dim_path)
    df = pd.read_parquet(staging_path)


    # pull just the country-related columns and collapse to one row per country
    dim_country = (
        df[["country_id", "country_code", "country_name"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )


    # sanity check: if country_id really identifies one country, the number of
    # unique rows here should match the number of unique country_id values in
    # the staging data. assert stops execution immediately (with the given
    # message) if that's ever not true, which flags a data-quality problem
    # rather than silently writing a broken dimension table.
    assert len(dim_country) == df["country_id"].nunique(), "Mismatch — investigate duplicates further"


    print(dim_country.head())
    print(f"Total unique countries: {len(dim_country)}")


    dim_path.parent.mkdir(parents=True, exist_ok=True)
    dim_country.to_parquet(dim_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {dim_path}, {len(dim_country)} rows")


    return dim_country




if __name__ == "__main__":
    from config import staging_dir, Dimension_dir

    staging_path = staging_dir / "ProcessedOpenAQ_platform.parquet"
    dim_path = Dimension_dir / "Dim_country.parquet"


    build_country_data(staging_path, dim_path)

