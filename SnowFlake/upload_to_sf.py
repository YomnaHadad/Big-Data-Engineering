import os
from pyspark.sql import SparkSession

# 1. Force root permissions
os.environ["HADOOP_USER_NAME"] = "root"

# 2. Reconnect to YARN (Using your original ETL configurations)
snowflake_packages = "net.snowflake:snowflake-jdbc:3.13.30,net.snowflake:spark-snowflake_2.12:2.12.0-spark_3.3"

spark = SparkSession.builder \
    .appName('Snowflake_Loader') \
    .master('yarn') \
    .config("spark.hadoop.fs.defaultFS", "hdfs://hadoop-namenode:9000") \
    .config("spark.hadoop.yarn.resourcemanager.hostname", "resourcemanager") \
    .config("spark.hadoop.yarn.resourcemanager.address", "resourcemanager") \
    .config("spark.hadoop.yarn.resourcemanager.scheduler.address", "resourcemanager") \
    .config("spark.jars.packages", snowflake_packages) \
    .getOrCreate()

BASE_PATH = "hdfs://hadoop-namenode:9000/user/root/output/"

# Snowflake Connection Options
sfOptions = { 
    "sfURL": "vudwvrf-hg36916.snowflakecomputing.com",
    "sfUser": "YomnaHALEEM",
    "sfPassword": "---", 
    "sfDatabase": "Diamonds_DB", 
    "sfSchema": "STAR_SCHEMA",
    "sfWarehouse": "Diamonds_WH",
    "sfRole": "ACCOUNTADMIN"
}

def load_to_snowflake(df, table_name):
    df.write \
        .format("snowflake") \
        .options(**sfOptions) \
        .option("dbtable", table_name) \
        .mode("append") \
        .save()

    print(f"{table_name} loaded successfully.")

load_to_snowflake(dim_cut_df, "DIM_CUT")
load_to_snowflake(dim_color_df, "DIM_COLOR")
load_to_snowflake(dim_clarity_df, "DIM_CLARITY")
load_to_snowflake(dim_date_df, "DIM_DATE")
load_to_snowflake(fact_df, "FACT_DIAMONDS")
