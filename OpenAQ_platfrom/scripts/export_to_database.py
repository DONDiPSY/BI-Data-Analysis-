import os
import pandas as pd
# Create a database connection engine in python
from sqlalchemy import create_engine, text
# Safely encode Special Character in String (Especially Username and Password)
from urllib.parse import quote_plus
# load environment variable from a dot env file into python
from dotenv import load_dotenv
# encrypting and decrypting sensitive data
from cryptography.fernet import Fernet

from config import Dimension_dir, Fact_dir


def get_engine(db_name="postgres"):
    """
    Build a SQLAlchemy engine for the given database, decrypting
    the username/password from environment variables along the way.
    """
    load_dotenv()

    key = os.getenv("DB_KEY").encode()
    encrypt_user = os.getenv("POST_USER").encode()
    encrypt_pass = os.getenv("POST_PASS").encode()

    cipher = Fernet(key)
    decrypt_user = cipher.decrypt(encrypt_user).decode()
    decrypt_pass = cipher.decrypt(encrypt_pass).decode()

    username = quote_plus(decrypt_user)
    password = quote_plus(decrypt_pass)

    return create_engine(
        f"postgresql+psycopg2://{username}:{password}@localhost:5432/{db_name}"
    )


def create_database_if_not_exists(db_name):
    """
    Connect to the default 'postgres' db and create db_name if it
    doesn't already exist. Uses AUTOCOMMIT since CREATE DATABASE
    can't run inside a transaction block.
    """
    engine = get_engine("postgres")
    with engine.connect() as conn:
        conn = conn.execution_options(isolation_level="AUTOCOMMIT")
        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE data_name = : name"),
            {"name": db_name},
        ).scalar()
        if not exists:
            conn.execute(text(f"CREATE DATABASE {db_name}"))
            print(f"Created database: {db_name}")
        else:
            print(f"Database already exists: {db_name}")
    engine.dispose()


def load_parquet_folder_to_sql(folder_path, engine):
    """
    Load every .parquet file in folder_path into its own table,
    named after the file stem (lowercased).
    """
    for parquet_file in folder_path.glob("*.parquet"):
        table_name = parquet_file.stem.lower()
        df = pd.read_parquet(parquet_file)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Loaded {table_name}")


def load_openaq_warehouse(db_name="openaq_warehouse"):
    """
    Full pipeline: ensure the warehouse database exists, then load
    all dimension and fact parquet files into it as tables.
    """
    create_database_if_not_exists(db_name)

    engine = get_engine(db_name)

    model = {
        "dimension_dir": Dimension_dir,
        "fact_dir": Fact_dir,
    }

    for folder_name, folder_path in model.items():
        print(folder_name, " : ", folder_path)
        load_parquet_folder_to_sql(folder_path, engine)

    engine.dispose()


if __name__ == "__main__":
    load_openaq_warehouse()