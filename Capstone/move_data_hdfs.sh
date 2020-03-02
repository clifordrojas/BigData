#!/bash/sh

cd /home/desktop/Desktop/BigData/Capstone/Ingestion/

hadoop fs -copyFromLocal neobi_api_producer.json /data
echo "copied neobi_api_producer to hdfs"

hadoop fs -copyFromLocal neobi_api_weed.json /data
echo "copied neobi_api_weed to hdfs"

