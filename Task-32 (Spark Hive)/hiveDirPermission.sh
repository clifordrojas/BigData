#!/bin/sh

hdfs dfs -mkdir -p /user/hive/warehouse

hdfs dfs -mkdir /tmp

hdfs dfs -chmod g+w /user/hive/warehouse

hdfs dfs -chmod g+w /tmp


