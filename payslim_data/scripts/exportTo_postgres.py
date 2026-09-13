import os
import pandas as pd
# Create a database connection  engine in python
from sqlalchemy import create_engine,text
# Safely encode Special character in string (especially Username and Passwords)
from urllib.parse import  quote_plus
# load environment variable from  a .env file into python
from dotenv import load_dotenv
#encrypting and decrypting sensitive data
from cryptography.fernet import Fernet

from Dipsy.OpenAQ_platfrom.scripts.export_to_database import DB_NAME
from config import Dim_Dir, Fact_Dir



# load environment variable
load_dotenv()
# Retrieve key and encrypted user and password from env
key = os.getenv("DB_KEY").encode()
encrypted_user = os.getenv("POST_USER").encode()
encrypted_pass = os.getenv("POST_PASS").encode()

# Decrypt Username and Pass with key
Cipher = Fernet(key)
decrypt_user = Cipher.decrypt(encrypted_user).decode()
decrypt_pass = Cipher.decrypt(encrypted_pass).decode()
# safely encode the username and password for  the url
username = quote_plus(decrypt_user)
password = quote_plus(decrypt_pass)
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/postgres")
conn = engine.connect()
conn = conn.execution_options(isolation_level="AUTOCOMMIT")
conn.execute(text("CREATE DATABASE Paysim_warehouse"))
conn.close()
engine.dispose()

conn = engine.connect()
conn = conn.execution_options(isolation_level="AUTOCOMMIT")
DB_NAME = "Paysim_warehouse"
conn.execute(text(f"CREATE DATABASE {DB_NAME} "))
conn.close()
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost:5432/{DB_NAME}")
# folder containing parquet files
model =  {
    "dim_dir" :Dim_Dir,
    "fact_dir": Fact_Dir
}

# load all parquet files
for foldername , folder_path  in model.items():
    print(foldername, " : ",  folder_path )
    # glob means scan the folder and give the files that contains parquet
    for parquet_file in folder_path.glob("*.parquet"):
        print(parquet_file)
        # save all files and stem files
        # stem means strip the extension and give the filename without parquet
        Paysim_Data_model = parquet_file.stem.lower()
        df = pd.read_parquet(parquet_file)
        df.to_sql(Paysim_Data_model, engine, if_exists="replace", index=False)
        print(f"Loaded{Paysim_Data_model}")


"""
with engine.connect() as conn:
    result = conn.execute(text("SELECT current_database();"))
    print(result.fetchone())
"""
