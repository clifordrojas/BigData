#!/bin/bash

cd 
start-dfs.sh
start-yarn.sh

hdfs dfs -mkdir /data
hdfs dfs -mkdir /tmp
hdfs dfs -mkdir /user

cd ~/Desktop/example.txt

#Copy file
hadoop fs -copyFromLocal notes/DailyTasks /data
