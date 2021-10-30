from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
with DAG(
    dag_id="first_python_dag",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    def print_array():
        import pandas as pd
        print(pd.__version__)
        return pd.__version__

    run_this = PythonOperator(
        task_id="print_the_context",
        python_callable=print_array,
    )