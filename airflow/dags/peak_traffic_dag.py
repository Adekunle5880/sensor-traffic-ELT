# peak_traffic_times_by_hour_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os

def run_dbt_model():
    os.system('dbt run --models peak_traffic_times_by_hour')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'peak_traffic_times_by_hour_dag',
    default_args=default_args,
    description='A DAG to run DBT model for peak traffic times by hour',
    schedule_interval=None,
)

run_dbt_task = PythonOperator(
    task_id='run_dbt_model',
    python_callable=run_dbt_model,
    dag=dag,
)
