from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime, timedelta


with DAG(
    dag_id="diamonds_big_data_etl",
    start_date=datetime(2026, 5, 5),
    schedule_interval='@daily', # Customized to run once a day
    catchup=False,
    description="End-to-End Diamonds ETL: HDFS -> Spark Star Schema -> Snowflake",
    tags=['spark', 'snowflake', 'hdfs']
) as dag:

    start_pipeline = EmptyOperator(task_id="start_pipeline")
    end_pipeline = EmptyOperator(task_id="end_pipeline")

    # 1. Ingest CSV batches into HDFS
    task_ingest_hdfs = BashOperator(
        task_id="ingest_data_to_hdfs",
        bash_command="""
        docker exec hadoop-namenode hdfs dfs -mkdir -p /data && \
        docker exec hadoop-namenode hdfs dfs -put -f /tmp/diamonds_*.csv /data/
        """
    )

    # 2. Run Spark transformation + star schema creation
    task_transform_spark = BashOperator(
        task_id="transform_to_star_schema",
        bash_command="""
        docker exec spark-jupyter spark-submit \
        --master yarn \
        /home/jovyan/work/notebooks/to_star_schema.py
        """
    )

    # 3. Verify output folders in HDFS
    task_verify_hdfs = BashOperator(
        task_id="verify_star_schema_output",
        bash_command="""
        docker exec hadoop-namenode hdfs dfs -ls /user/root/output/
        """
    )

    # 4. Load dimension and fact tables into Snowflake
    task_load_snowflake = BashOperator(
        task_id="load_to_snowflake",
        bash_command="""
        docker exec spark-jupyter spark-submit \
        --master yarn \
        --packages net.snowflake:spark-snowflake_2.12:2.12.0-spark_3.3,net.snowflake:snowflake-jdbc:3.13.30 \
        /home/jovyan/work/notebooks/spark-warehouse/snowflake.py
        """
    )

    # Define the precise execution order
    start_pipeline >> task_ingest_hdfs >> task_transform_spark >> task_verify_hdfs >> task_load_snowflake >> end_pipeline
