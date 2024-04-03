
import datetime
from airflow import DAG

from apache.airflow.providers.clickhouse.operators.ClickhouseOperator import ClickhouseOperator


with DAG(
    dag_id='example_clickhouse_operator',
    start_date=datetime.datetime(2021, 1, 1),
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=['example','clickhouse'],
    catchup=False,
    template_searchpath='$AIRFLOW_HOME/include'
) as dag:

    # set sql direct in the code section
    echo = ClickhouseOperator(
        task_id='echo_clickhouse',
        sql="select 'Hello, Airflow!'",
        click_conn_id='clickhouse_default'
    )

    echo
    