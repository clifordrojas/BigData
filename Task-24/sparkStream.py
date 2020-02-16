import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import requests
from io import StringIO
#from hdfs import InsecureClient
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer


def readAPI():
    output = StringIO()
    # fileWriter = open("data.json", "w+")
    counter = 0
    stringIO = StringIO()
    while counter <= 2:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        stringIO.write(str(response.json()) + "\n")
        # print(str(response.json())+"\n")
        counter += 1

    data = stringIO.getvalue()
    output.close()
    return data
def sendKafkaMessage(producer,lines):
    producer.send("ChuckNorris", bytes(lines, 'utf-8'))
    # producer.flush()

def handler(message):
    records = message.collect()
    for record in records:
        producer.send('spark.out', str(record))
        # producer.flush()


if __name__ == '__main__':
    data = readAPI()
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    #Send Kafka Message using Kafka Producer
    sendKafkaMessage(producer,data)

    #Spark Stream
    sc = SparkContext.getOrCreate()
    ssc = StreamingContext(sc, 10)

    brokers = ""
    topic = ""

    broker = "localhost:9092"
    topic = ["ChuckNorris"]
    stream = KafkaUtils.createDirectStream(ssc, topic, {"metadata.broker.list": brokers})
    stream.foreachRDD(handler)

    ssc.start()
    ssc.awaitTermination()



