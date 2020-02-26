
import requests
from io import StringIO
import json

from pyspark.sql.functions import split

from Weed import Weed
from pyspark import SparkContext, SparkConf
from pyspark.sql import  SparkSession,Row,functions
from pyspark.rdd import RDD
import pandas as pd


def read_file_json(file_name):
    with open(file_name+".json") as f:
        json_data = json.load(f)
        return json_data
def drop_columns_weed(dataframe):
    weed = dataframe.select("name", "ccc", "type", "thc", "price", "metaDescription", "brand", "producer")
    return weed
def drop_columns_producer(dataframe):
    producer = dataframe.select("name","ccc","location","phone","email")
    return  producer

def create_spark_df(file):
    to_pdf = pd.DataFrame(file)
    to_sdf = spark.createDataFrame(to_pdf)
    return to_sdf



if __name__ == '__main__':

    sc = SparkContext("local", "My Context")
    spark = SparkSession(sc)

    weed = read_file_json("neobi_api_weed")
    producer = read_file_json("neobi_api_producer")

    weed_df = drop_columns_weed(create_spark_df(weed))
    producer_df = drop_columns_producer(create_spark_df(producer))

    # dict_keys(['image', 'ccc', 'phone', 'link', 'name', 'location', 'email'])
    # weed_df.select("producer").foreach(lambda x: print(x[0]["ccc"]))
    # weed_df.select(functions.col("name"), functions.map_values(functions.col("producer")).show()
    # for i in weed_df.schema.fieldNames():
    #     print(i)
    weed_df.withColumn('Producer2',weed_df['producer']["ccc"]).show()

    weed_df.show()
    producer_df.show()
