from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql import SparkSession
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.10.34,org.apache.hadoop:hadoop-aws:2.7.2 pyspark-shell'
#Access from local
# s3 = boto3.resource("s3")
# bucket = s3.Bucket("BUCKET")
# obj = bucket.Object(key="All_the_Jokes.txt")
# response = obj.get()
#
# text = response["Body"].read()
# print(text)

conf = (SparkConf()
        .setAppName("S3 Configuration Test")
        .set("spark.executor.instances", "1")
        .set("spark.executor.cores", 1)
        .set("spark.executor.memory", "2g"))
# Settting up the configuration to access Amazon S3
sc = SparkContext(conf=conf)
#sc._jsc.hadoopConfiguration().set("fs.s3.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")
#sc._jsc.hadoopConfiguration().set("fs.s3n.impl", "org.apache.hadoop.fs.s3native.NativeS3FileSystem")


# Set log level to off for faster performance of the terminal
# sc.setLogLevel("OFF")
# Sql context to run queries
sqlContext = SQLContext(sc)
# Spark Session to create dataframes and use the read.Json method after proper configuration of Amazon S3
ss = SparkSession(sc)

file = ss.read.json("s3n://2020clifordrojas/All_the_Jokes.txt")
run_sql = file.createOrReplaceTempView("funny_table")
query = sqlContext.sql("Select categories,created_at,id, value from funny_table")
query.schema
query.show()
query.write.partitionBy("id").parquet("s3n://2020clifordrojas/output")

