#!/bin/bash
cd ~
echo "Y
" > Yes.txt

sudo apt install python3-pip < Yes.txt
sudo pip3 install apache-airflow < Yes.txt

export PATH=$PATH:/home/`/usr/bin/whoami`/.local/bin
airflow initdb

rm Yes.txt


