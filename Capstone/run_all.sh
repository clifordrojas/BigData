#!/bash/sh

cd /home/desktop/Desktop/BigData/Capstone

#Start dependencies
source Automation/run_dependencies_first.sh

cd /home/desktop/Desktop/BigData/Capstone

#Create table 
source Automation/run_hive_mkTable.sh

cd /home/desktop/Desktop/BigData/Capstone

#Get ingestion data
source Automation/run_ingestion.sh

cd /home/desktop/Desktop/BigData/Capstone

#Move to hdfs
source Automation/move_data_hdfs.sh

cd /home/desktop/Desktop/BigData/Capstone

#Spark processing using scala
source Automation/process_data.sh

cd /home/desktop/Desktop/BigData/Capstone

#Load data into hive
source Automation/load_data_hive.sh

cd /home/desktop/Desktop/BigData/Capstone

hive -e "show tables";
hive -e "select * from weed";
hive -e "drop table weed"

cd /home/desktop/Desktop/BigData/Capstone

source remove_hdfs_data.sh
