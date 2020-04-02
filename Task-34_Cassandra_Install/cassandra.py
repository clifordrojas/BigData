
import os
from pyspark.sql import SparkSession, SQLContext, DataFrame, Column
from pyspark.sql.types import StructType, StructField, StringType,IntegerType

os.environ["PYSPARK_SUBMIT_ARGS"] = "--packages com.datastax.spark:spark-cassandra-connector_2.11:2.4.2 --conf spark.cassandra.connection.host=127.0.0.1 pyspark-shell"

# SETUP SPARK SESSION
spark:SparkSession = SparkSession.builder \
                            .master( "local[*]" ) \
                            .appName( "Cassandra-data-task-34" ) \
                            .getOrCreate()

csv_df = spark.read.format("csv").option("header", "false").load("file:///home/desktop/Desktop/csv_file.csv")
csv_df.registerTempTable('csv_temp_table')

named_df = spark.sql( "select uuid() as csv_id, _c1 as age, _c2 as first_name, _c3 as last_name from csv_temp_table")
named_df.show()

named_df.write\
    .format("org.apache.spark.sql.cassandra")\
    .mode( "append" )\
    .options( table="csv_data", keyspace="clifordtesting" )\
    .save()

schema = StructType([
                StructField( "json_id",  StringType() ),
                StructField( "age",  StringType() ),
                StructField( "first_name", StringType() ),
                StructField( "last_name", StringType() )
         ]
         )

csv_df = spark.read.schema(schema).format("json").load("file:///home/desktop/Desktop/json_file.json")
csv_df.registerTempTable('json_temp_table')

temp = spark.sql("select * from json_temp_table")
temp.show()
named_df = spark.sql( "select uuid() as json_id, age,first_name,last_name from json_temp_table")
named_df.show()

# named_df.write\
#     .format("org.apache.spark.sql.cassandra")\
#     .mode( "append" )\
#     .options( table="json_data", keyspace="clifordtesting" )\
#     .save()
#
# csv_read = spark.read\
#                 .format("org.apache.spark.sql.cassandra")\
#                 .options(table="csv_data", keyspace="clifordtesting")\
#                 .load()
# csv_read.show()