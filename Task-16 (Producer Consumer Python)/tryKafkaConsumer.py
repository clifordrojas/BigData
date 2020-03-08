from kafka import KafkaConsumer
import multiprocessing
import time 
import sys
import time

bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
consumer = KafkaConsumer(topicName, group_id='group1', bootstrap_servers=bootstrap_servers,
                         auto_offset_reset='earliest')

def read():
	try:
		for message in consumer:
			print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
	except:
		print("failed")

p = multiprocessing.Process(target=read, name="read", args=())
p.start()

time.sleep(10)

p.terminate()
p.join()
