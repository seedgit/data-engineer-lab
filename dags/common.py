from datetime import datetime, timedelta

DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 3, 26),
    'retry_delay': timedelta(minutes=1),
}
