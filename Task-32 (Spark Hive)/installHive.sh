#!/bin/sh

#Get hive 2.3.6
wget "http://www.trieuvan.com/apache/hive/hive-2.3.6/apache-hive-2.3.6-bin.tar.gz"

#Unpack Hive
tar -xzvf apache-hive-2.3.6-bin.tar.gz

sudo cp -r apache-hive-2.3.6-bin /opt/

cd

export "HIVE_HOME=/opt/apache-hive-2.3.6-bin" >> .bash_profile
export "PATH=$PATH:/opt/apache-hive-2.3.6-bin" >> .bash_profile

source .bash_profile


cd $HIVE_HOME
cd ..
sudo chmod 777 apache-hive-2.3.6-bin




