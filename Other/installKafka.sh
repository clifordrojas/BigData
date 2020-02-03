#!/bin/sh

cd /opt
#Get Kafka
sudo wget http://apache.mirrors.hoobly.com/kafka/2.3.1/kafka_2.12-2.3.1.tgz
#Extract the file
sudo tar -xzvf kafka_2.12-2.3.1.tgz
#Remove zip file
sudo rm kafka_2.12-2.3.1.tgz
#Update the bash profile
echo -e '\n#Kafka Home'  >> ~/.bash_profile
echo 'export KAFKA_HOME=/opt/kafka_2.12-2.3.1' >> ~/.bash_profile
echo 'export PATH=$PATH:$KAFKA_HOME/bin' >> ~/.bash_profile


