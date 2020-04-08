#!/bin/bash

#Installing HBase
wget https://apache.mirror.gtcomm.net/hbase/2.2.4/hbase-2.2.4-bin.tar.gz

tar -zxvf hbase-2.2.4-bin.tar.gz

sudo cp -r hbase-2.2.4 /opt/

cd 

echo -e "#Set up Hbase\nexport HBASE_HOME=/opt/hbase-2.2.4\nexport PATH=$PATH:/opt/hbase-2.2.4/bin" >> .bash_profile

