import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

name = "movies"
with DAG(
    dag_id=name,
    catchup=False,
    start_date=datetime.datetime(2021, 1, 1),
    schedule_interval="*/5 * * * *",  # Every 5 minutes
    tags=["scrape_id:TEST"],
) as dag:

    scrape = BashOperator(
        dag=dag,
        task_id=f"scrape_{name}",
        bash_command="python /opt/airflow/src/scrapes/movies/scrape.py",
    )

    etl = BashOperator(
        dag=dag,
        task_id=f"etl_{name}",
        bash_command="python /opt/airflow/src/scrapes/movies/etl.py",
    )

    scrape >> etl
