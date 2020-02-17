from kafka import KafkaProducer
import json
import requests
from io import StringIO
import subprocess

# from names import get_full_name

output = StringIO()

fileWriter = open("data.json", "w+")
counter = 0
stringIO = StringIO()
while counter <= 1:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    stringIO.write(str(response.json())+"\n")
    print(str(response.json())+"\n")
    counter += 1
data = stringIO.getvalue()
fileWriter.write(data[0:len(data)])
bash_command = 'hadoop fs -copyFromLocal data.json /data'
process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
output,error = process.communicate()

bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer = KafkaProducer()
ack = producer.send(topicName, bytes(data,'utf-8'))
metadata = ack.get()
print(metadata.topic)
print(metadata.partition)

stringIO.close()
fileWriter.close()
