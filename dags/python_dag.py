from airflow.decorators import dag, task
from datetime import datetime
import json

default_args = {
    'start_date': datetime(2021, 1, 1)
}
@dag('python_dag', schedule_interval='@daily', default_args=default_args, catchup=False)
def taskflow():
    @task
    def extract():
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        return json.loads(data_string)
    
    @task
    def transfrom(order_data):
        print(type(order_data))
        total_order_value = 0
        for value in order_data.values():
            total_order_value += value
        return {"total_order_value": total_order_value}

    @task
    def loading():
        print('Loading')

    transfrom(extract())

dag = taskflow()