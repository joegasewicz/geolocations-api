import os
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

DB_NAME = "location_etl_db"
DB_PORT = 5433
DB_USERNAME = "admin"
DB_PASSWORD = "admin"
DB_HOST = "host.docker.internal"


def get_pg_conn() -> str:
    return f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def dump_dataframe(ti: TaskInstance):
    transform_file_path = ti.xcom_pull(task_ids="transform", key="transform_file_path")
    engine = create_engine(get_pg_conn())
    df = pd.read_csv(transform_file_path, index_col=0)
    # database
    metadata = MetaData()
    locations_table = Table("locations", metadata,
        Column("id", Integer, primary_key=True),
        Column("town", String(255)),
        Column("longitude", Float(8)),
        Column("latitude", Float(8)),
        Column("iso_3166_1", String(255)),
        Column("country", String(255)),
    )
    try:
       with engine.connect() as conn:
           metadata.create_all(conn)
           df_dict = df.to_dict("records")
           locations_insert = locations_table.insert().values(df_dict)
           conn.execute(locations_insert)
           print("locations data inserted successfully.")
    except SQLAlchemyError as err:
        print(f"[Full Error]: {str(err)}")
        print(f"Error dumping {transform_file_path}")
    finally:
        engine.dispose()


def extract(ti: TaskInstance):
    file_path = "/etl-data/Major_Towns_and_Cities_Dec_2015_Boundaries_V2_2022_140358522642712462.csv"
    if pd is None:
        raise ModuleNotFoundError("Pandas not installed!")
    ti.xcom_push(key="file_path", value=file_path)


def transform(ti: TaskInstance):
    transform_file_path = "/etl-data/uk_ons_locations_transform.csv"
    file_path = ti.xcom_pull(task_ids="extract", key="file_path")
    df = pd.read_csv(file_path)
    df = df.drop(columns=[
        "OBJECTID",
        "TCITY15CD",
        "BNG_E",
        "BNG_N",
        "Shape__Area",
        "Shape__Length",
        "GlobalID",
    ])
    df = df.rename(columns={
        "TCITY15NM": "town",
        "LONG": "longitude",
        "LAT": "latitude",
    })
    df["iso_3166_1"] = "GB-ENG"
    df["country"] = "England"
    df.to_csv(transform_file_path)
    ti.xcom_push(key="transform_file_path", value=transform_file_path)


default_args = {
    "owner": "geolocations-api",
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id="uk-ons-locations-dag-v1",
    default_args=default_args,
    description="DAG for loading ONS locations data to postgres",
    schedule_interval="@once",
    start_date=datetime(2025, 1, 5),
    catchup=False,
) as dag:

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="chmod a+x /etl-data/Major_Towns_and_Cities_Dec_2015_Boundaries_V2_2022_140358522642712462.csv",
    )

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    drop_table_task = SQLExecuteQueryOperator(
        task_id="drop_locations_table",
        conn_id="location_etl_db",
        sql="""
        DROP TABLE IF EXISTS locations;
        """,
    )

    create_tables_task = SQLExecuteQueryOperator(
        task_id="load",
        conn_id="location_etl_db",
        sql="""
        CREATE TABLE IF NOT EXISTS locations (
            id SERIAL PRIMARY KEY,
            town VARCHAR(255) NOT NULL,
            longtitude double precision,
            latitude double precision,
            iso_3166_1 VARCHAR(255) NOT NULL,
            country VARCHAR(255) NOT NULL
        );
        """
    )

    dump_dataframe_task = PythonOperator(
        task_id="dump_dataframe",
        python_callable=dump_dataframe,
    )

    # bash_task.set_downstream(extract_task)
    extract_task.set_downstream(transform_task)
    transform_task.set_downstream(drop_table_task)
    # drop_table_task.set_downstream(create_tables_task)
    drop_table_task.set_downstream(dump_dataframe_task)
    # create_tables_task.set_downstream(dump_dataframe_task)
