#!/bin/bash

wget https://downloads.apache.org/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz

tar -xvf  sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz

sudo cp -r sqoop-1.4.7.bin__hadoop-2.6.0 /opt/sqoop-1.4.7

cd
#Set up Sqoop
echo -e '#Sqoop setup\nexport SQOOP_HOME=/opt/sqoop-1.4.7\nexport PATH=$PATH:/opt/sqoop-1.4.7/bin' >> .bash_profile

