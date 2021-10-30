FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3.6 python3-pip
RUN mkdir /opt/airflow
ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
RUN pip install apache-airflow==2.2.0 --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.2.0/constraints-3.6.txt
RUN pip install pandas beautifulsoup4 sklearn

RUN airflow db init
RUN airflow users create \
    --username admin \
    --password password \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org