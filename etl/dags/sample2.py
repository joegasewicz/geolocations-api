"""
We can pass data between different tasks using Xcoms
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/taskinstance/index.html
Warning!: Max size of xcoms is 48kb (don't pass Panda dataframes!
"""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.models.taskinstance import TaskInstance
from airflow.operators.python import PythonOperator


def get_name(ti: TaskInstance):
    ti.xcom_push(key="first_name", value="Joe")
    ti.xcom_push(key="last_name", value="Doe")

def get_cat_name(ti: TaskInstance):
    ti.xcom_push(key="cat_name", value="Sumi")


def greet(age: int, ti: TaskInstance):
    first_name = ti.xcom_pull(task_ids="get_name", key="first_name")
    last_name = ti.xcom_pull(task_ids="get_name", key="last_name")
    cat_name = ti.xcom_pull(task_ids="get_cat_name", key="cat_name")
    print(f"Hello {first_name} {last_name}! You are nealy {age} years old!"
          f"How is {cat_name} doing?")


default_args = {
    "owner": "geolocations-api",
    "retries": 5,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id="python-operator-dag-v9",
    default_args=default_args,
    description="DAG for loading ONS locations data to postgres",
    schedule_interval="@once",
    start_date=datetime(2025, 1, 5)
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={"age": 21}
    )

    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name,
    )

    task3 = PythonOperator(
        task_id="get_cat_name",
        python_callable=get_cat_name,
    )

    task2.set_downstream(task1)
    task3.set_downstream(task1)
