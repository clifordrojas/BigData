#!/bin/bash

cd 
start-dfs.sh
start-yarn.sh

cd ~/Desktop/BigData/Task-14 (Read API store HDFS)

#Pull Data using scala
scalac getChuckNorris.scala
scala getChuckNorris
#Pull Data using python
python3 getChuckNorris.py 


#Move files to hdfs //Ensure HDFS is on using 
hadoop fs -copyFromLocal data.json /data
hadoop fs -copyFromLocal scalaData.json /data
