from airflow import DAG
from airflow.operators.python import PythonOperator
     
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

