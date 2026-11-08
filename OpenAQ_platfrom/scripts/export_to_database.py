import os
import pandas as pd
# Create a database connection engine in python
from sqlalchemy import create_engine, text, inspect
# Safely encode Special Character in String (Especially Username and Password)
from urllib.parse import quote_plus
# load environment variable from a dot env file into python
from dotenv import load_dotenv
# encrypting and decrypting sensitive data
from cryptography.fernet import Fernet

from config import Dimension_dir, Fact_dir,  Bridge_dir


def get_engine(db_name="postgres"):
    """
    Build a SQLAlchemy engine for the given database, decrypting
    the username/password from environment variables along the way.
    But does not create a physical database
    """
    load_dotenv()

    # Retrieve the encrypted credentials
    key = os.getenv("DB_KEY").encode()
    encrypt_user = os.getenv("POST_USER").encode()
    encrypt_pass = os.getenv("POST_PASS").encode()

    # Decrypt encrypted credentials  is the variable as the key
    cipher = Fernet(key)
    decrypt_user = cipher.decrypt(encrypt_user).decode()
    decrypt_pass = cipher.decrypt(encrypt_pass).decode()

    # Encode special characters
    username = quote_plus(decrypt_user)
    password = quote_plus(decrypt_pass)

    # create and return your SqlAlchemy engine
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
    # establish a connection with the engine
    with engine.connect() as conn:
        conn = conn.execution_options(isolation_level="AUTOCOMMIT")
        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = :name"),
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

        df.to_sql(table_name, engine, if_exists="append", index=False)
        print(f"Loaded {table_name}")

def truncate_warehouse_tables(engine):

    with engine.begin() as conn:

        conn.execute(text("""
            TRUNCATE TABLE
                bridge_location_instrument,
               bridge_location_license,
                dim_country,
                dim_instrument,
                dim_license,
                dim_location,
                dim_owner,
                dim_parameter,
                dim_provider,
                dim_sensor,
                fact_activity
            RESTART IDENTITY;
        """))



def load_openaq_warehouse(db_name="openaq_warehouse"):
    """
    Full pipeline: ensure the warehouse database exists, then load
    all dimension and fact parquet files into it as tables.
    """
    # ensure the database exits if it  doesn't create it
    create_database_if_not_exists(db_name)

    # connect to the warehouse database
    engine = get_engine(db_name)
    try:
        # clear existing warehouse records
        truncate_warehouse_tables(engine)


        #  a dict that consist of file directories
        model =  {
        "dimension_dir": Dimension_dir,
        "fact_dir": Fact_dir,
        "bridge" : Bridge_dir }
        # loop through the directories and pass  each to loading function
        for folder_name, folder_path in model.items():
            print(folder_name, " : ", folder_path)
            # insert records into now empty tables
            load_parquet_folder_to_sql(folder_path, engine)
    finally:
        engine.dispose()


if __name__ == "__main__":
    load_openaq_warehouse()