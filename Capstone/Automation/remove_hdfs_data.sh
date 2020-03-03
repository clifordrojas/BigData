#!/bash/sh
cd
#Remove data 
hdfs dfs -rm -r /user/hive/warehouse/w*

hdfs dfs -rm -r /user/hive/warehouse/df_hive

hdfs dfs -ls /user/hive/warehouse/

#Remove Ingested Files
cd /home/desktop/Desktop/BigData/Capstone/Ingestion
rm neo*

