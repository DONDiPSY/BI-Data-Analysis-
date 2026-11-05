import pandas as pd
from pathlib import Path
def build_owner_data(staging_path, dim_owner_p):
    """
    Build owner dimension from cleaned OpenAQ staging data
    :param staging_path:
    :param dim_owner_p:
    :return:
    dim_owner: pd.DataFrame
    one row per unique owner id  with owner_name
    """
    dim_owner_path =Path(dim_owner_p)
    df= pd.read_parquet(staging_path)
    # pull just the owner_id and owner_name
    dim_owner =  df[["owner_id", "owner_name"]].drop_duplicates(subset="owner_id").reset_index(drop=True)
    dim_owner.insert(0, "owner_key", dim_owner.index + 6540)
    dim_owner["owner_key"] = dim_owner["owner_key"].astype(int)
    # investigating if owner_id unique for accessing owner_name (Sanity Check )
    assert len(dim_owner) == df["owner_id"].nunique(), "Mismatch — investigate duplicates further"
    print(dim_owner.head())
    print(f"Total unique owners: {len(dim_owner)}")

    dim_owner_path.parent.mkdir(parents=True, exist_ok=True)
    dim_owner.to_parquet(dim_owner_path, engine="pyarrow",index=False, compression="snappy")
    print(f"Cleaned and processed data is written to {dim_owner_path}, {len(dim_owner)} rows")


    return dim_owner

if __name__ == "__main__":
    from config import staging_dir, Dimension_dir

    staging_path = staging_dir / "processed_sensorsOpenAQ_platform.parquet"
    dim_owner_path= Dimension_dir/"Dim_owner.parquet"

    build_owner_data(staging_path,dim_owner_path)