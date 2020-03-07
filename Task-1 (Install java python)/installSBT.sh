#!/bin/bash
echo "Y
" > Yes.txt

echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823
sudo apt-get update < Yes.txt
sudo apt-get install sbt < Yes.txt

rm Yes.txt
