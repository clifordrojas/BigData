#!/bin/bash

#Start Zookeeper
cd $KAFKA_HOME
bin/zookeeper-server-start.sh config/zookeeper.properties > ~/Desktop/zookeeper.log 

cd ~/Desktop/BigData/Task-16*

#Create producer
nohup python3 tryKafka.py> ~/Desktop/pykafka_producer.log &

#Create Consumer
python3 tryKafkaConsumer.py > ~/Desktop/pykafka_consumer.log



