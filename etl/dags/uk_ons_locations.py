import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.models.taskinstance import TaskInstance
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import pandas as pd


def extract(ti: TaskInstance):
    file_path = "/data/Major_Towns_and_Cities_Dec_2015_Boundaries_V2_2022_140358522642712462.csv"
    if pd is None:
        raise ModuleNotFoundError("Pandas not installed!")
    if file_path is None:
        raise FileNotFoundError(f"File not found: {file_path}")
    ti.xcom_push(key="file_path", value=file_path)


def transform(ti: TaskInstance):
    transform_file_path = "/data/uk_ons_locations_transform.csv"
    file_path = ti.xcom_pull(task_ids="extract", key="file_path")
    df = pd.read_csv(file_path)
    df = df.drop(columns=["OBJECTID", "TCITY15CD", "BNG_E", "BNG_N", "Shape__Area", "Shape__Length", "GlobalID"])
    df = df.rename(columns={
        "TCITY15NM": "towns",
        "LONG": "longitude",
        "LAT": "latitude",
    })
    df["iso-3166-1"] = "GB-ENG"
    df["country"] = "England"
    df.to_csv(transform_file_path)
    ti.xcom_push(key="transform_file_path", value=transform_file_path)


default_args = {
    "owner": "geolocations-api",
    "retries": 5,
    "retry_delay": timedelta(seconds=5),
}


with DAG(
    dag_id="uk-ons-locations-dag-v3",
    default_args=default_args,
    description="DAG for loading ONS locations data to postgres",
    schedule_interval="@once",
    start_date=datetime(2025, 1, 5),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    create_tables_task = SQLExecuteQueryOperator(
        task_id="load",
        conn_id="location_etl_db",
        sql="""
        CREATE TABLE IF NOT EXISTS locations (
            id SERIAL PRIMARY KEY,
            towns VARCHAR(255) NOT NULL,
            longtitude double precision,
            latitude double precision,
        );
        """
    )

    extract_task.set_downstream(transform_task)
    transform_task.set_downstream(create_tables_task)
