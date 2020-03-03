#!/bash/sh

#Start Airflow
airflow webserver -D
echo "Airflow Started"


airflow scheduler
echo "Airflow Scheduler started"
