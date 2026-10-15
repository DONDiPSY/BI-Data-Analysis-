import pandas as pd
from airflow.sdk import dag, task
import pendulum
from Dipsy.OpenAQ_platfrom.scripts.Extract_openAQ import extract_data
from Dipsy.OpenAQ_platfrom.scripts.cleaned_OpenAQ import process_openaq_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_Country import build_country_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_owner import build_owner_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_instrument import  build_instrument_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_license import build_license_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_sensor import build_sensor_data
from Dipsy.OpenAQ_platfrom.scripts.Fact_Station_Activity import build_fact_data
from Dipsy.OpenAQ_platfrom.scripts.export_to_database import load_openaq_warehouse
from Dipsy.OpenAQ_platfrom.scripts.config import Dimension_dir, Fact_dir, Raw_dir, staging_dir
from Dipsy.OpenAQ_platfrom.scripts.Dim_provider import build_provider_data



@dag(
    schedule ="@daily",
    start_date = pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup= False,
    tags = ["api", "postgres", "warehouse", "openaq"],
)

def openaq_pipeline():

    @task
    def extract_openaq(**context) -> str:
        """
                Fetch/save the raw OpenAQ JSON for this run and return its path
                as a plain string (XComs should carry small, serializable values,
                not Path objects or DataFrames).
            """
        # stamp the filename with Airflow's logical date so each run is traceable
        run_stamp = context["logical_date"].strftime("%Y%m%d_%H%M%S")
        raw_json_path = Raw_dir/f"Raw_OpenAQ_{run_stamp}.json"
        # ... your actual API call / download logic writes to raw_path here ...
        extract_data(save_path=raw_json_path)
        return str(raw_json_path)

    @task
    def Clean_and_stage(raw_json_path:str)->str:
        staging_path = staging_dir/"ProcessedOpenAQ_platform.parquet"
        process_openaq_data(raw_json_path =raw_json_path, staging_path=staging_path)
        return str(staging_path)

    @task
    def make_country_dim(staging_path:str)->str:
        dim_path = Dimension_dir/"Dim_country.parquet"
        build_country_data(staging_path=staging_path, dim_path=dim_path)
        return str(dim_path)
    @task
    def make_owner_dim(staging_path:str)->str:
        dim_owner_path = Dimension_dir/"Dim_owner.parquet"
        build_owner_data(staging_path, dim_owner_path)
        return str(dim_owner_path)

    @task
    def make_instrument_dim(staging_path: str) -> str:
        dim_instrument_path = Dimension_dir / "Dim_instrument.parquet"
        build_instrument_data(staging_path, dim_instrument_path)
        return str(dim_instrument_path)

    @task
    def make_license_dim(staging_path: str) -> str:
        dim_license_path = Dimension_dir / "Dim_license.parquet"
        build_license_data(staging_path, dim_license_path)
        return str(dim_license_path)

    @task
    def make_station_dim(staging_path:str)->str:
        dim_sensor_path= Dimension_dir/"Dim_sensor.parquet"
        build_sensor_data(staging_path,  dim_sensor_path)
        return str( dim_sensor_path)
    @task
    def make_provider_dim(staging_path:str)->str:
        dim_provider_path= Dimension_dir/"Dim_provider.parquet"
        build_provider_data(staging_path,dim_provider_path)
        return str(dim_provider_path)

    @task
    def make_fact(staging_path:str, country_path:str, owner_path:str,
                  provider_path:str, instrument_path, license_path,station_path:str)->str:
        dim_tables ={
            "dim_country" : pd.read_parquet(country_path),
            "dim_owner" : pd.read_parquet(owner_path),
            "dim_provider" : pd.read_parquet(provider_path),
            "dim_instrument" : pd.read_parquet(instrument_path),
            "dim_license" : pd.read_parquet(license_path),
            "dim_station" : pd.read_parquet(station_path)
        }
        fact_path = Fact_dir/"Fact_Activity.parquet"
        build_fact_data(staging_path,dim_tables, fact_path)
        return str(fact_path)

    real_raw_path = extract_openaq()
    staging_path = Clean_and_stage(real_raw_path)

    country_path = make_country_dim(staging_path)
    owner_path = make_owner_dim(staging_path)
    provider_path = make_provider_dim(staging_path)
    instrument_path = make_instrument_dim(staging_path)
    license_path = make_license_dim(staging_path)
    station_path = make_station_dim(staging_path)

    fact_path= make_fact(staging_path, country_path, owner_path, provider_path, instrument_path, license_path,station_path)

    @task
    def export_tto_database() :
        load_openaq_warehouse()

    load_task = export_tto_database()
    fact_path >> load_task

openaq_pipeline()