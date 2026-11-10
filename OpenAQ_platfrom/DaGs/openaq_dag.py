import pandas as pd
from airflow.sdk import dag, task
import pendulum
from Dipsy.OpenAQ_platfrom.scripts.Extract_openAQ import extract_data
from Dipsy.OpenAQ_platfrom.scripts.cleaned_OpenAQ import process_openaq_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_location import build_location_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_Country import build_country_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_parameter import build_parameter_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_owner import build_owner_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_instrument import  build_instrument_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_license import build_license_data
from Dipsy.OpenAQ_platfrom.scripts.Dim_sensor import build_sensor_data
from Dipsy.OpenAQ_platfrom.scripts.Fact_Station_Activity import build_fact_data
from Dipsy.OpenAQ_platfrom.scripts.export_to_database import load_openaq_warehouse
from Dipsy.OpenAQ_platfrom.scripts.config import Dimension_dir, Fact_dir, Raw_dir, staging_dir, Bridge_dir
from Dipsy.OpenAQ_platfrom.scripts.Dim_provider import build_provider_data
from Dipsy.OpenAQ_platfrom.scripts.bridge_location_instrument import build_loc_instrument_data
from Dipsy.OpenAQ_platfrom.scripts.bridge_location_license import build_bridge_loc_license_data

default_args = {
    "owner": "data_engineering",
    "retries": 2,
    "retry_delay": pendulum.duration(minute=5),
}


@dag(
    dag_id ="openaq_data_pipeline",
    default_args=default_args,
    description="Extract stage and OpenAQ data",
    schedule ="@daily",
    start_date = pendulum.datetime(2026, 10, 1, tz="UTC"),
    catchup= False,
    max_active_runs=1,
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
    # build staging file  by make use of dict
    @task
    def stage_openaq(raw_json_path:str)->dict:

        staging_paths = {
            "instrument": str(staging_dir / "processed_instrumentOpenAQ_platform.parquet"),
            "license" : str(staging_dir / "processed_licenseOpenAQ_platform.parquet"),
            "sensor" : str(staging_dir / "processed_sensorsOpenAQ_platform.parquet"),
        }
        process_openaq_data(raw_json_path, staging_paths)
        return  staging_paths




    @task
    def make_location_dim(staging_path: str) -> str:
        dim_location_path = Dimension_dir / "Dim_location.parquet"
        build_location_data(staging_path=staging_path, dim_path= dim_location_path)
        return str( dim_location_path)

    @task
    def make_country_dim(staging_path:str)->str:
        dim_country_path = Dimension_dir/"Dim_country.parquet"
        build_country_data(staging_path=staging_path, dim_path=dim_country_path)
        return str(dim_country_path)
    @task
    def make_owner_dim(staging_path:str)->str:
        dim_owner_path = Dimension_dir/"Dim_owner.parquet"
        build_owner_data(staging_path, dim_owner_path)
        return str(dim_owner_path)

    @task
    def make_parameter_dim(staging_path: str) -> str:
        dim_parameter_path = Dimension_dir / "Dim_parameter.parquet"
        build_parameter_data(staging_path, dim_parameter_path)
        return str(dim_parameter_path)

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
    def make_sensor_dim(staging_path:str)->str:
        dim_sensor_path= Dimension_dir/"Dim_sensor.parquet"
        build_sensor_data(staging_path,  dim_sensor_path)
        return str( dim_sensor_path)
    @task
    def make_provider_dim(staging_path:str)->str:
        dim_provider_path= Dimension_dir/"Dim_provider.parquet"
        build_provider_data(staging_path,dim_provider_path)
        return str(dim_provider_path)

    @task
    def make_bridge_instrument(staging_path:str)->str:
        bridge_instrument_path = Bridge_dir/"Bridge_location_instrument.parquet"
        build_loc_instrument_data(staging_path, bridge_instrument_path)
        return str(bridge_instrument_path)

    @task
    def make_bridge_license(staging_path:str)->str:
        bridge_license_path = Bridge_dir/"Bridge_location_license.parquet"
        build_bridge_loc_license_data(staging_path, bridge_license_path)
        return str(bridge_license_path)


    @task
    def make_fact(staging_path,location_path,country_path, owner_path, parameter_path,
                  provider_path, instrument_path, license_path, sensor_path)->str:



        dim_tables ={
            "dim_location" : pd.read_parquet(location_path),
            "dim_country" : pd.read_parquet(country_path),
            "dim_owner" : pd.read_parquet(owner_path),
            "dim_provider" : pd.read_parquet(provider_path),
            "dim_parameter" : pd.read_parquet(parameter_path),
            "dim_instrument" : pd.read_parquet(instrument_path),
            "dim_license" : pd.read_parquet(license_path),
            "dim_sensor" : pd.read_parquet(sensor_path)
        }
        fact_path = Fact_dir/"Fact_Activity.parquet"
        build_fact_data(staging_path, fact_path, dim_tables)
        return str(fact_path)

    real_raw_path = extract_openaq()
    staging_paths = stage_openaq(real_raw_path)
    output_path1 = staging_paths["instrument"]
    output_path2 =staging_paths["license"]
    output_path3 = staging_paths["sensor"]

    location_path = make_location_dim(output_path1)
    country_path = make_country_dim(output_path3)
    owner_path = make_owner_dim(output_path3)
    parameter_path = make_parameter_dim(output_path3)
    provider_path = make_provider_dim(output_path3)
    instrument_path = make_instrument_dim(output_path1)
    license_path = make_license_dim(output_path2)
    sensor_path = make_sensor_dim(output_path3)

    # Bridge tables
    bridge_instrument_path = make_bridge_instrument(output_path1)
    bridge_license_path = make_bridge_license(output_path2)

    fact_path= make_fact(output_path1,output_path2,output_path3, location_path,country_path,owner_path,
                        parameter_path,provider_path, instrument_path, license_path, sensor_path)

    @task
    def export_tto_database() :
        load_openaq_warehouse()

    load_task = export_tto_database()
    [fact_path, bridge_instrument_path, bridge_license_path] >> load_task

openaq_pipeline()

