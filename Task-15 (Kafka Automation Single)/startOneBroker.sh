#!/bin/bash


cd $KAFKA_HOME

#Start Zookeeper
nohup bin/zookeeper-server-start.sh config/zookeeper.properties > ~/Desktop/zookeeper.log & 

# Start broker
nohup bin/kafka-server-start.sh config/server.properties ~/Desktop/broker.log&
 


