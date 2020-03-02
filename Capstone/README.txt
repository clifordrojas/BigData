Please follow the commands to execute properly.

1) Start dependencies: run_dependencies_first
-Starts Hadoop
-Starts Airflow

2)Create Tables in hive: run_hive_mktable
-Creates weed table

3)Ingest data: run_ingestion.sh
-Use python to ingest data

4)Move Data: move_data_to_hdfs
-Move ingested data to hdfs

5)Run Spark Processing Scala: pending

6)Load Data: load_data_hive.sh
-loads hdfs data into hive table

7)Verify 
-hive -e "show tables";
-hive -e "select * from weed";

8)Remove to clean 
-hive -e "drop table weed"
-source remove_hdfs_data.sh



