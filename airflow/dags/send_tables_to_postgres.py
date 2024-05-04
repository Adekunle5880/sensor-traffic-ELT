from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from populate_db import send_to_postgres

# define airflow dag
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 5, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'send tables to postgres',
    default_args = default_args,
    description = 'A DAG to send tables to PostgreSQL',
    schedule_interval = None,
)

send_to_postgres_task = PythonOperator(
    task_id = 'send_to_postgres_task',
    python_callable = send_to_postgres,
    dag=dag,
)

send_to_postgres_task