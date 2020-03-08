#!/bin/bash

nohup airflow webserver -p 8080&
nohup airflow scheduler &
echo "Airflow started"
