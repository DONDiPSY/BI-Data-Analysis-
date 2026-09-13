import pandas as pd
from pathlib import Path



def build_provider_data(staging_path, provider_path):

    dim_provider_path =Path(provider_path)
    df = pd.read_parquet(staging_path)
    # drop duplicate with resetting the dataframe
    Dim_provider = df[["provider_id","provider_name"]].drop_duplicates().reset_index(drop= True)
    # investigating if provider_id unique for accessing provider_name
    assert len(Dim_provider) == df["provider_id"].nunique(), "Mismatch — investigate duplicates further"
    print(Dim_provider.head())
    print(f"Total unique owners: {len(Dim_provider)}")
    dim_provider = Dim_provider[["provider_id","provider_name"]]
    # create a directory folder
    dim_provider_path.parent.mkdir(parents=True, exist_ok=True)
    dim_provider.to_parquet(dim_provider_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {dim_provider_path}, {len(dim_provider)} rows")

    return dim_provider

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    staging_path = staging_dir / "ProcessedOpenAQ_platform.parquet"
    dim_provider_path=Dimension_dir/"Dim_provider.parquet"

    build_provider_data(staging_path, dim_provider_path)