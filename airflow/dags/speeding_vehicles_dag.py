# speeding_vehicles_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os

def run_dbt_model():
    os.system('dbt run --models speeding_vehicles')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'speeding_vehicles_dag',
    default_args=default_args,
    description='A DAG to run DBT model for speeding vehicles',
    schedule_interval=None,
)

run_dbt_task = PythonOperator(
    task_id='run_dbt_model',
    python_callable=run_dbt_model,
    dag=dag,
)
