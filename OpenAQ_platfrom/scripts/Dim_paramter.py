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
    dim_paramter = (df[['parameter_id','parameter_name','units','display_name']]
                    .drop_duplicates().reset_index(drop=True))


    assert len(dim_paramter) == df["parameter_id"].nunique(), "Mismatch — investigate duplicates further"


    print(dim_paramter.head())
    print(f"Total unique Parameters: {len(dim_paramter)}")

    dim_path.parent.mkdir(parents=True, exist_ok=True)
    dim_paramter.to_parquet(dim_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Clean and processed data is written to {dim_path}, {len(dim_paramter)} rows")

    return dim_paramter

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    staging_path = staging_dir/ "ProcessedOpenAQ_platform.parquet"
    dim_path = Dimension_dir / "Dim_paramter.parquet"

    build_parameter_data(staging_path, dim_path)
