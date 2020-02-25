import requests
from io import StringIO
import json
from Weed import Weed
from pyspark import SparkContext, SparkConf
from pyspark.sql import  SparkSession,Row,functions
from pyspark.rdd import RDD

import pandas as pd


def read_neobi_api():
    url = "https://neobi.p.rapidapi.com/api/products"
    querystring = {"count":"100","htmlDescription":"false","sort":"created","page":"1","rev":"v1.6"}
    headers = {
        'x-rapidapi-host': "neobi.p.rapidapi.com",
        'x-rapidapi-key': "e11ecc4264msh3835ca68b292c91p176f38jsn8f7e9a70df5b"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def read_file_json(file_name):
    with open(file_name+".json") as f:
        json_data = json.load(f)
        return json_data

def create_local_file(data):
    with open("neobi_api.json", "w") as local_file:
        json.dump(data,local_file)


# data = read_neobi_api()
# json_data = json.loads(data.text)
# create_local_file(json_data)
file_name = "neobi_api"
data = read_file_json(file_name)

key_words = ["name","producer","eqWeight","thc","price"]
print(data[0].keys())
print(data[0])

list_of_weed = []
for x in range(100):
    weed = Weed(data[x]["name"],data[x]["type"],data[x]["thc"],data[x]["price"],data[x]["brand"],data[x]["currency"],data[x]["producer"]["name"])
    list_of_weed.append(weed)


df = pd.DataFrame(data)
sc = SparkContext("local", "My Context")
spark = SparkSession(sc)
spark_df = spark.createDataFrame(df)
query = spark_df.select("name","thc","cbd","price")

print(query.show())

