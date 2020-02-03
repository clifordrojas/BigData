#!/bin/sh

#Ensure Java 
cd /opt

#Get Java 8 
sudo wget -O jdk-8u221-linux-x64.tar.gz -c --content-disposition "https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"

#Unpack Java 8
sudo tar -xzvf jdk-8u221-linux-x64.tar.gz

#Remove zip
sudo rm jdk-8u221-linux-x64.tar.gz

#Move to home dir
cd ~/

#Add to bash profile
echo -e "export JAVA_HOME=/opt/jdk1.8.0_221\nexport PATH=$PATH:$JAVA_HOME/bin" >> .bash_profile


