#!/bash/sh

cd

#Hadoop Start
start-dfs.sh

start-yarn.sh
echo "Hadoop Started"

#Start Airflow
airflow webserver -D
echo "Airflow Started"