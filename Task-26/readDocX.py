#########
import textract
import string
# import pyspark
import os

from docutils.nodes import inline
from pyspark import SparkContext, SparkConf
from pyspark.rdd import RDD
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import *
from pyspark.sql import Row
from pyspark.sql import functions as f
# from pyspark.sql.functions import lit
from nltk.corpus import stopwords
from string import punctuation

from sqlalchemy import asc, desc


def cleanWord(word):
    '''
    This method will take a word and remove all leading and trailing symbols i.e. ,.$
    :param word:
    :return: Returns a lowercase the word with no leading/trailling chars
    '''
    cleanWord = word.translate(str.maketrans("", "", string.punctuation))
    cleanWord = cleanWord.rstrip()
    cleanWord = cleanWord.lower()

    return cleanWord

def cleanProfile(profile):


    words_List = profile.split(" ")
    for words in words_List:
        words = cleanWord(words)

        # print(words)
        if words in bad_words or words in ["using"]:
            pass
            # print("Not adding the word:\t{}".format(words))
        elif words == "":
            pass
        elif not words.isalpha():  # If it is not in the alphabet don't add
            pass
        else:
            list_word.append(words)
    return words_List
def profile_to_RDD(list_words):
    data = sc.parallelize(list_words)

    return data

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

def readFiles(dir,entries):
    """
    This will read the doc(x) files in the directory
    :param dir: Directory to read
    :param entries: Names of the files including extentions
    :return: two lists
    """
    profile_complete = []
    profile_List = []
    list_word = []
    for x in range(len(entries)):
        try:
            docx_file = textract.process(dir + entries[x]).decode("utf-8")

            profile_complete.append(docx_file)

            line_arr = docx_file.split("\n")
            for lines in line_arr:
                if lines == "":
                    pass
                    # print("Not Adding empty")
                else:
                    profile_List.append(lines)

            words_List = docx_file.split(" ")
            for words in words_List:
                words = cleanWord(words)

                # print(words)
                if words in bad_words or words in ["using"]:
                    pass
                    # print("Not adding the word:\t{}".format(words))
                elif words == "":
                    pass
                elif not words.isalpha():  # If it is not in the alphabet don't add
                    pass
                else:
                    list_word.append(words)
            # break

        except:
            print("File cannot be read: {} \t\tvalue of x:{}".format(entries[x], x))
            # docx_file = textract.process(dir + entries[x])
    return profile_complete,profile_List,list_word

if __name__ == '__main__':

# Assign the OS path that has all the files
    dir = '/home/cliff/Downloads/profiles/'
    # This gets all the names in that directory
    entries = os.listdir(dir)
    # print(entries)
    # os path join
    # Keywords wanted
    keywords = ["kafka", "spark", "emr", "mr", "mapreduce", "flume", "aws"]
    # List of words that match the keyword
    list_word = []
    # Bad words
    bad_words = stopwords.words('english')
    # List of lines
    profile_List = []
    # Set of profiles to compare
    profile_complete = []

    profile_complete,profile_List,list_word = readFiles(dir,entries)


    sc = SparkContext("local", "First App")
    sc.setLogLevel("OFF")
    spark = SparkSession(sc)
    data = sc.parallelize(list_word)
    clean_rdd: RDD = data.map(lambda word: (word, 1))
    reduce_rdd: RDD = clean_rdd.reduceByKey(lambda v1, v2: v1 + v2)
    df_rdd = reduce_rdd.sortBy(lambda x: x[1], ascending=False)
    add_all = df_rdd.values().sum()
    weighted_frequency = df_rdd.values().map(lambda x: (x / add_all) * 100)
    row = Row("Frequency")  # Or some other column name
    weighted_frequency = weighted_frequency.map(row)

    df = spark.createDataFrame(df_rdd).toDF("Word", "Count")
    three_column = df.withColumn("Frequency", (df.Count / df.count())).sort(f.col("Frequency").desc())
    three_column = three_column.withColumn("Frequency", f.round(three_column['Frequency'], 2))
    print(three_column.show())
    # -------- -----------------Everything Above Works------------------------------------------------#

    profile0 = cleanProfile(profile_complete[0])
    profile0_RDD = cleanRDD(profile_to_RDD(profile0),bad_words)
    profile0_RDD = mapRDD(profile0_RDD)
    profile0_RDD = reduceRDD(profile0_RDD)
    profile0_RDD = sortRDD(profile0_RDD)


    profile1 = cleanProfile(profile_complete[1])
    profile1_RDD = cleanRDD(profile_to_RDD(profile1),bad_words)
    profile1_RDD = mapRDD(profile1_RDD)
    profile1_RDD = reduceRDD(profile1_RDD)
    profile1_RDD = sortRDD(profile1_RDD)


    profile2 = cleanProfile(profile_complete[2])
    profile2_RDD = cleanRDD(profile_to_RDD(profile2),bad_words)
    profile2_RDD = mapRDD(profile2_RDD)
    profile2_RDD = reduceRDD(profile2_RDD)
    profile2_RDD = sortRDD(profile2_RDD)

    profile3 = cleanProfile(profile_complete[3])
    profile3_RDD = cleanRDD(profile_to_RDD(profile3),bad_words)
    profile3_RDD = mapRDD(profile3_RDD)
    profile3_RDD = reduceRDD(profile3_RDD)
    profile3_RDD = sortRDD(profile3_RDD)

    profile0_df = spark.createDataFrame(profile0_RDD).toDF("Profile0_Words","Profile0_count")
    profile0_df = profile0_df.withColumn("Frequency", (profile0_df.Profile0_count / profile0_df.count())).sort(f.col("Frequency").desc())
    profile0_df = profile0_df.withColumn("Frequency", f.round(profile0_df['Frequency'], 2))
    profile1_df = spark.createDataFrame(profile1_RDD).toDF("Profile1_Words","Profile1_count")
    profile1_df = profile1_df.withColumn("Frequency", (profile1_df.Profile1_count / profile1_df.count())).sort(f.col("Frequency").desc())
    profile1_df = profile1_df.withColumn("Frequency", f.round(profile1_df['Frequency'], 2))
    profile2_df = spark.createDataFrame(profile2_RDD).toDF("Profile2_Words","Profile2_count")
    profile2_df = profile2_df.withColumn("Frequency", (profile2_df.Profile2_count / profile2_df.count())).sort(f.col("Frequency").desc())
    profile2_df = profile2_df.withColumn("Frequency", f.round(profile2_df['Frequency'], 2))
    profile3_df = spark.createDataFrame(profile3_RDD).toDF("Profile3_Words","Profile3_count")
    profile3_df = profile3_df.withColumn("Frequency", (profile3_df.Profile3_count / profile3_df.count())).sort(f.col("Frequency").desc())
    profile3_df = profile3_df.withColumn("Frequency", f.round(profile3_df['Frequency'], 2))

    join1 = profile0_df.join(profile1_df).where(profile0_df[0] == profile1_df[0])
    join2 = join1.join(profile2_df).where(join1[0] == profile2_df[0])
    join3 = join2.join(profile3_df).where(join2[0] == profile3_df[0])
    join3 = join3.orderBy("Profile0_count",ascending=False)
    print(join3.show())


"""
Shuffle : Move data from one server to another
Physical and Logical plan from spark.

Use this command for antiword dependencies
sudo apt-get install antiword


"""
