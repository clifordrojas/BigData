#!/bash/sh

#Remove data 
hdfs dfs -rm -r /user/hive/warehouse/weed

hdfs dfs -rm -r /user/hive/warehouse/df_hive

hdfs dfs -ls /user/hive/warehouse/
