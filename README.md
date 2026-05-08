# Big-Data-Engineering-Project
## ETL Pipline

1. Write a script to Take the file and send it to another location As it's being sent in real time in batches 
2. store these data into hdfs and apply some transformations 
3. build star schema 
4. load the data into snowflake DWH 
5. But all of this into airflow 

--------------------------------
### Project & Dataset Outline:
building an end-to-end ETL pipeline for processing and analyzing diamond sales data using modern Big Data technologies. The pipeline simulates real-time batch ingestion, processes and transforms the data using distributed computing, models it using a Star Schema design, and loads the final analytical data into a cloud data warehouse for reporting and business intelligence purposes.

diamonds dataset containing attributes such as `carat`, `cut`, `color`, `clarity`, `dimensions`, `depth`, and `price`. Data is ingested in batches and stored in **Apache Hadoop Distributed File System (HDFS)**. The processing layer is implemented using **Apache Spark**, where data cleaning, validation, and feature engineering transformations are applied.

After transformation, the data is modeled into a **dimensional warehouse structure using a Star Schema**.

The transformed data warehouse tables are then loaded into **Snowflake** to support scalable analytics and business intelligence operations. Finally, the entire workflow is orchestrated and automated using **Apache Airflow**, enabling scheduled ingestion, transformation, and loading tasks within a reproducible ETL pipeline architecture.

The project demonstrates practical implementation of:
  - Distributed data ingestion and storage
  - Batch and streaming-oriented ETL concepts
  - Big Data processing with Spark
  - Dimensional data modeling using Star Schema
  - Cloud data warehousing
  - Workflow orchestration and automation
  - Scalable analytical pipeline design

--------------------------------

### setting the env up
- docker-compose up -d  >> Pull and create the env
- docker ps  >> see the contrainer
- docker exec -it hadoop-namenode bash   >> Enter the container hadoop-namenode
- hdfs dfs -mkdir -p /data   >> create a directory
- hdfs dfs -put /path/to/your/diamonds_part_1.csv /data/
- hdfs dfs -ls /data   >> list the files in the container (verify the files in data folder)
- docker logs spark-jupyter
- sudo apt install hdfs-cli

### Copy file into container From the host Then moving it inside container 
- docker cp diamonds_part_1.csv hadoop-namenode:/tmp/
- docker cp diamonds_part_2.csv hadoop-namenode:/tmp/
- docker cp diamonds_part_3.csv hadoop-namenode:/tmp/

```
hdfs dfs -put /tmp/diamonds_part_1.csv /data/
sleep 10
hdfs dfs -put /tmp/diamonds_part_2.csv /data/
sleep 10
hdfs dfs -put /tmp/diamonds_part_3.csv /data/
```
### Change HDFS Permissions
- hdfs dfs -mkdir -p /user/jovyan   >>  Create a home directory for the user jovyan
- hdfs dfs -chown jovyan:jovyan /user/jovyan    >>  Give the user jovyan ownership of that directory- 

### About the data
- **carat**: Weight of the diamond in carats, - (0.2–5.01 carats)
- **cut**: Quality of the cut (categorical: Fair, Good, Very Good, Premium, Ideal)
- **color**: Diamond color grade (D best → J worst)
- **clarity**: Internal/external imperfections (I1 worst → IF best)
- **depth**: Total depth percentage (indicates proportion and affects light return)
- **table**: Table percentage (width of top facet relative to widest point)
- **price**: Price in US dollars
- **x, y, z**: Physical dimensions in millimeters (length, width, depth)

### Star schema modeling

>> **numerical** >> carat, depth, table, price, x, y, z

>> **categorical** >> cut, color, clarity

```
           dim_cut
              |
              |
dim_color — fact_diamonds — dim_clarity

```
### Snowflake 

### Airflow
Airflow UI at: <http://localhost:18080>
