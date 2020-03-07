#!/bin/bash

nohup echo "I'm producer" | nc -l 5555 > ~/Desktop/producer.txt &

nohup echo "I'm Consumer" | nc localhost 5555 > ~/Desktop/consumer.txt &


