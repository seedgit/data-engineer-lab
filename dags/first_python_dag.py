from datetime import datetime, time

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="first_python_dag",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    def my_sleeping_function(random_base):
        """This is a function that will run within the DAG execution"""
        time.sleep(random_base)

    # Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively
    task = PythonOperator(
        task_id='sleep_for_1',
        python_callable=my_sleeping_function,
        op_kwargs={'random_base': float(1) / 10},
    )

    task2 = PythonOperator(
        task_id='sleep_for_2',
        python_callable=my_sleeping_function,
        op_kwargs={'random_base': float(2) / 10},
    )

    task3 = PythonOperator(
        task_id='sleep_for_3',
        python_callable=my_sleeping_function,
        op_kwargs={'random_base': float(3) / 10},
    )

    task >> task2 >> task3