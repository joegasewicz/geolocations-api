from datetime import datetime, timedelta

from airflow import DAG
from airflow.models.taskinstance import TaskInstance
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import (
    create_engine,
    types,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Float,
)

from utils.config import Config
from utils.database import get_pg_conn
from utils.load import Load


config = Config()


def dump_dataframe(ti: TaskInstance):
    aus_transform_file_path = ti.xcom_pull(task_ids="transform", key="aus_transform_file_path")
    engine = create_engine(get_pg_conn(config))
    df = pd.read_csv(aus_transform_file_path, index_col=0)
    # database
    load = Load(engine=engine, df_dict=df, file_path=aus_transform_file_path)
    load.run()


def extract(ti: TaskInstance):
    file_path = "/etl-data/Australia_Entire_Dataset.xlsx"
    if pd is None:
        raise ModuleNotFoundError("Pandas not installed!")
    ti.xcom_push(key="file_path", value=file_path)


def transform(ti: TaskInstance):
    aus_transform_file_path = "/etl-data/Australia_Entire_Dataset.csv"
    file_path = ti.xcom_pull(task_ids="extract", key="file_path")
    df = pd.read_excel(file_path)
    df = df.drop(columns=[
        "Unnamed: 0",
        "id"
    ])
    df = df.rename(columns={
        "name": "town",
    })
    df["country"] = "Australia"
    df.to_csv(aus_transform_file_path)
    ti.xcom_push(key="aus_transform_file_path", value=aus_transform_file_path)


default_args = {
    "owner": "geolocations-api",
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id="aus-kaggle-dag-v2",
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

    dump_dataframe_task = PythonOperator(
        task_id="dump_dataframe",
        python_callable=dump_dataframe,
    )

    extract_task.set_downstream(transform_task)
    transform_task.set_downstream(dump_dataframe_task)
