#!/bin/bash

#Get
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1804-4.0.18.tgz

#Unpack
tar -xzvf mongodb-linux-x86_64-ubuntu1804-4.0.18.tgz

#Copy
sudo cp -r mongodb-linux-x86_64-ubuntu1804-4.0.18 /opt
 
#Remove Files
rm -r mongodb-linux-x86_64-ubuntu1804-4.0.18

#Update bash_profile
cd 
echo -e "#MongoDB Setup \nexport MONGODB_HOME=/opt/mongodb\nexport PATH=$PATH:/opt/mongodb/bin" >> .bash_profile 
source .bash_profile

#Give Permission
cd $MONGODB_HOME 
cd ..
sudo chmod 777 -R mongodb

echo "MongoDB Install Completed"
