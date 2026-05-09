from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="simple_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    description="Simple Diamonds ETL Pipeline"
) as dag:

    ingest_data = BashOperator(
        task_id="ingest_data_to_hdfs",
        bash_command="""
        echo 'Ingesting diamonds data into HDFS'
        """
    )

    transform_data = BashOperator(
        task_id="transform_data_with_spark",
        bash_command="""
        echo 'Running Spark transformations'
        """
    )

    load_to_snowflake = BashOperator(
        task_id="load_to_snowflake",
        bash_command="""
        echo 'Loading star schema tables into Snowflake'
        """
    )

    ingest_data >> transform_data >> load_to_snowflake
