#!/bash/sh
cd
cd /home/desktop/Desktop/BigData/Capstone/Ingestion/

hdfs dfs -mkdir /user/desktop/

hadoop fs -copyFromLocal neobi_api_producer.json /user/desktop/
echo "copied neobi_api_producer to hdfs"

hadoop fs -copyFromLocal neobi_api_weed.json /user/desktop/
echo "copied neobi_api_weed to hdfs"

