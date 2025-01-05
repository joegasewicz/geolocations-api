# ETL
ETL pipelines with Apache Airflow.

⚠️Currently, airflow pypi package is only compatible with Python `3.12`

### Setup (for MacOS only)
Running airflow for the first tme
1. First update the postgres volume's absolute path manually
2. Run airflow with docker compose:
```
make airflow-init
make airflow
```
From then on, you just need to run the following:
```
make airflow
```
3. Make sure Rust & Cargo are installed on your machine.
4. Make sure you have Python version `3.12` installed.
5. Run `pipenv install`. We only install `apache-airflow` for the typings when developing airflow DAGS.

### Load
After extraction, the data is loaded into the postgres `location_etl_db` database running on port `5433` 