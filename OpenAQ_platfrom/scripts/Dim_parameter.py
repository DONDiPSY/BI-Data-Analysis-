import pandas as pd
from pathlib import Path

def build_parameter_data(staging_path, dim_path):
    """
        Build the country dimension table from the cleaned OpenAQ staging data.


        Parameters
        ----------
        staging_path : str or Path
            Path to the cleaned staging Parquet file (the output of
            process_openaq_data).
        dim_path : str or Path
            Full output path (including filename) for the paramter dimension
            Parquet file.


        Returns
        -------
        dim_paramter : pd.DataFrame
            One row per unique unit, with 'parameter_id', 'parameter_name',
            and 'display_name'.
        """
    dim_path = Path(dim_path)
    df = pd.read_parquet(staging_path)
    dim_parameter = df[['parameter_id','parameter_name','parameter_units','parameter_display_name']].drop_duplicates('parameter_id').reset_index(drop=True)
    dim_parameter.insert(0, "parameter_key", dim_parameter.index + 4430)
    dim_parameter["parameter_key"] = dim_parameter["parameter_key"].astype(int)


    assert len(dim_parameter) == df["parameter_id"].nunique(), "Mismatch — investigate duplicates further"


    print(dim_parameter.head())
    print(f"Total unique Parameters: {len(dim_parameter)}")

    dim_path.parent.mkdir(parents=True, exist_ok=True)
    dim_parameter.to_parquet(dim_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Clean and processed data is written to {dim_path}, {len(dim_parameter)} rows")

    return dim_parameter

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    staging_path = staging_dir/ "processed_sensorsOpenAQ_platform.parquet"
    dim_path = Dimension_dir / "Dim_parameter.parquet"

    build_parameter_data(staging_path, dim_path)
