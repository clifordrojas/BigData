import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.rdd import RDD
from pyspark.sql import functions as f
import os
import string
from nltk.corpus import stopwords


def readSCFile(file_name, DIR="/home/cliff/notes/Task-23/"):
    """
    Reads file given the name and directory. Default is '/home/cliff/notes/Task-23/'
    :param file_name: Give name of the text file to read in string value. If using from outside source provide directory.
    :return: returns an RDD from the textFile.
    """
    file_rdd: RDD = sc.textFile(DIR + file_name)
    return file_rdd

def readSparkFile(file_name, DIR = "/home/cliff/notes/Task-23/"):
    """
    Reads a file using Spark Session
    :param file_name: String name of the files. ex: example.txt
    :param DIR: By default takes creator dir but can pass any dir.
    :return: Spark DataFrame obj
    """
    spark_file = spark.read.text(DIR+file_name)

    return spark_file

def cleanRDD(rdd_to_clean,words_not_to_include = stopwords.words('english')):
    """
    This function will receive a list of words that you want to filter out from the RDD. Along with that it will filter
    out the empty strings and return a split rdd. in the form of ["word1","word2"..]

    :param rdd_to_clean: RDD to be cleaned
    :param words_not_to_include: Words that you want to filter out.
    :return:
    """
    #Remove punctuation
    clean_rdd = rdd_to_clean.map(lambda x: "".join(e.lower() for e in x if e not in string.punctuation))

    #Split the rdd
    split_rdd = clean_rdd.flatMap(lambda line: line.split(" "))

    #Remove stop words and empty string
    split_rdd = split_rdd.filter(lambda word: word not in words_not_to_include and word != "")

    return split_rdd


def cleanDF(spark_df):
    """
    This will take a spark dataframe and convert it to an rdd to process the data.
    :param spark_df: Takes a spark dataframe
    :return: rdd that's been cleaned.
    """

    #Remove punctuation
    clean_df = spark_df.rdd.flatMap(lambda new_line: new_line)
    clean_df = cleanRDD(clean_df)
    return clean_df



def mapRDD(rdd_to_map):
    """
    Creates tuple pairs one a key and the other a value ("key",1)
    :param rdd_to_map: Makes a key for all the words and assigns teh value of 1
    :return: Returns the set of rdd keys
    """
    mapped_rdd = rdd_to_map.map(lambda word: (word, 1))

    return mapped_rdd


def reduceRDD(map_rdd):
    """
    This will reduce the mapped keys so only one unique key exist and adds the values of duplicate keys.

    :param map_rdd: Spark Context RDD
    :return: Spark Context RDD with unique keys
    """
    reduced_rdd = map_rdd.reduceByKey(lambda v1, v2: v1 + v2)
    return reduced_rdd


def sortRDD(reduce_rdd):
    """
    This will sort the rdd so the count is at it's highest examples:("hello",10000)
    :param reduce_rdd: SPark Context RDD
    :return: Sorted RDD
    """
    sorted_rdd = reduce_rdd.sortBy(lambda x: x[1], ascending=False)
    return sorted_rdd




if __name__ == '__main__':
    # This will be the working directory for the files
    DIR = '/home/cliff/notes/Task-23/'

    # Files
    DIR_ARRAY = os.listdir(DIR)
    print("These are the files in the directory:", DIR_ARRAY)

    # Set up Spark
    sc = SparkContext("local", "My Context")
    spark = SparkSession(sc)

    #Bad Words
    BAD_WORDS = stopwords.words('english')

    #Open Files
    file_rdd = readSCFile(DIR_ARRAY[0]) #Caesar
    file_spark1 = readSparkFile(DIR_ARRAY[2]) #Bible
    file_spark2 = readSparkFile(DIR_ARRAY[3]) #Macbeth

    #Clean the file
    clean_rdd = cleanRDD(file_rdd,BAD_WORDS)
    clean_df_1 = cleanDF(file_spark1)
    clean_df_2 = cleanDF(file_spark2)


    #Map the files
    map_rdd = mapRDD(clean_rdd)
    clean_df_1 = mapRDD(clean_df_1)
    clean_df_2 = mapRDD(clean_df_2)

    #Reduce RDD
    reduce_rdd = reduceRDD(map_rdd)
    clean_df_1 = reduceRDD(clean_df_1)
    clean_df_2 = reduceRDD(clean_df_2)

    #Sort RDD
    sort_rdd = sortRDD(reduce_rdd)
    clean_df_1 = sortRDD(clean_df_1)
    clean_df_2 = sortRDD(clean_df_2)

    #Create dataframe
    rdd_to_df = spark.createDataFrame(sort_rdd).toDF("Caesar_Words","Caesar_count")
    dataframe_1 = spark.createDataFrame(clean_df_1).toDF("Bible_Words","Bible_Count")
    dataframe_2 = spark.createDataFrame(clean_df_2).toDF("Macbeth_Words","Macbeth_Count")

    #Join the tables
    join1 = rdd_to_df.join(dataframe_1).where(rdd_to_df[0] == dataframe_1[0])
    join2 = join1.join(dataframe_2).where(join1[2] == dataframe_2[0])

    print(join2.show())

