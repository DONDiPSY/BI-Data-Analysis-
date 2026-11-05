import pandas as pd
from pathlib import Path



def build_provider_data(staging_path, provider_path):

    dim_provider_path =Path(provider_path)
    df = pd.read_parquet(staging_path)
    # drop duplicate with resetting the dataframe
    Dim_provider = df[["provider_id","provider_name"]].drop_duplicates("provider_id").reset_index(drop= True)
    Dim_provider.insert(0,"provider_key", Dim_provider.index + 5050)
    Dim_provider["provider_key"] = Dim_provider["provider_key"].astype(int)
    # investigating if provider_id unique for accessing provider_name
    assert len(Dim_provider) == df["provider_id"].nunique(), "Mismatch — investigate duplicates further"

    print(f"Total unique owners: {len(Dim_provider)}")

    # create a directory folder
    dim_provider_path.parent.mkdir(parents=True, exist_ok=True)
    Dim_provider.to_parquet(dim_provider_path, engine="pyarrow", index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {dim_provider_path}, {len(Dim_provider)} rows")
    print(Dim_provider.head())
    return Dim_provider

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir
    staging_path = staging_dir / "processed_sensorsOpenAQ_platform.parquet"
    dim_provider_path=Dimension_dir/"Dim_provider.parquet"

    build_provider_data(staging_path, dim_provider_path)