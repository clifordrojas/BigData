#!/bin/bash
cd /opt

#download
sudo wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz

sudo chmod 755 /opt/

# unzip
sudo tar -xf Python-3.6.9.tgz
sudo rm Python-3.6.9.tgz

sudo chmod 755 /opt/
sudo ln -s /usr/bin/python3 /usr/bin/python
