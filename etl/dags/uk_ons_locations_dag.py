from datetime import datetime, timedelta


from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "geolocations-api",
    "retries": 5,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id="uk-ons-locations-v4",
    default_args=default_args,
    description="DAG for loading ONS locations data to postgres",
    schedule_interval="@once",
    start_date=datetime(2025, 1, 5)
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello Joe!",
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo 2nd task!",
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo Hey I am task 3!!!!",
    )

    task1.set_downstream(task2)
    task1.set_downstream(task3)
