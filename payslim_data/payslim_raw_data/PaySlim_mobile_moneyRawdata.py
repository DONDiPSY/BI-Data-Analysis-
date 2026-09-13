# import operating system
# where username and key is stored on my machine
import os
from dotenv import load_dotenv

# At this point KAGGLE_USERNAME and KAGGLE_KEY
# now exist in os.environ for this process ✅
load_dotenv()
username = os.getenv("KAGGLE_USERNAME")
key = os.getenv("KAGGLE_KEY")

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
# checking for verification of api username and password
api.authenticate()
dataset_slug = "ealaxi/paysim1"
try:
    api.dataset_download_files(dataset_slug, path="payslim_raw_data", unzip=True)
    print("Dataset downloaded successfully")
except Exception as Code_Crash:
    print(f"Error: {Code_Crash}")

