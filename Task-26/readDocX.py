
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


def cleanWord(word):
    '''
    This method will take a word and remove all leading and trailing symbols i.e. ,.$
    :param word:
    :return: Returns a lowercase the word with no leading/trailling chars
    '''
    cleanWord = word.translate(str.maketrans("","",string.punctuation))
    cleanWord = cleanWord.rstrip()
    cleanWord = cleanWord.lower()

    return cleanWord


#Assign the OS path that has all the files
dir = '/home/cliff/Downloads/profiles/'
#This gets all the names in that directory
entries = os.listdir(dir)
# print(entries)
#os path join
#Keywords wanted
keywords = ["kafka", "spark", "emr", "mr", "mapreduce", "flume", "aws"]
#List of words that match the keyword
list_word = []
#Bad words
bad_words = stopwords.words('english')
#List of lines
profile_List = []
#Set of profiles to compare

for x in range(len(entries)):
    """
    Iterate through the whole file(s) and add the words that match the key word for all .doc or .docx files in the
    directory.
    """
    try:
        docx_file = textract.process(dir + entries[x]).decode("utf-8")


        line_arr = docx_file.split("\n")
        for lines in line_arr:
            if lines == "":
                print("Not Adding empty")
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
            elif not words.isalpha(): #If it is not in the alphabet don't add
                pass
            else:
                list_word.append(words)
        # break

    except:
        print("File cannot be read: {} \t\tvalue of x:{}".format(entries[x],x))
        # docx_file = textract.process(dir + entries[x])



sc = SparkContext("local", "First App")
sc.setLogLevel("OFF")
spark = SparkSession(sc)
data = sc.parallelize(list_word)
clean_rdd:RDD = data.map(lambda word: (word,1))
reduce_rdd:RDD = clean_rdd.reduceByKey(lambda v1,v2: v1+v2 )
df_rdd = reduce_rdd.sortBy(lambda x: x[1], ascending = False )
add_all = df_rdd.values().sum()
weighted_frequency = df_rdd.values().map(lambda x: (x/add_all)*100)
row = Row("Frequency") # Or some other column name
weighted_frequency = weighted_frequency.map(row)

df = spark.createDataFrame(df_rdd).toDF("Word","Count")
three_column = df.withColumn("Frequency",(df.Count/df.count())).sort(f.col("Frequency").desc())
three_column = three_column.withColumn("Frequency",f.round(three_column['Frequency'],2))
#-------------------------Everything Above Works------------------------------------------------#
#List of lines Query
f = open("Lines.txt", "w")
for x in profile_List:
    f.write(x+"\n")
f.close()
# profile_1_data = sc.parallelize(get_lines_from_profileList).map(lambda word: "".join(w for w in word if w not in punctuation)).map(lambda word: (word,1))\
#     .reduceByKey(lambda v1,v2: v1+v2 )\
#     .sortBy(lambda x: x[1], ascending = False )
# dataFrame = spark.createDataFrame(profile_1_data).toDF("Profile_1","Profile_1_Count")

print(three_column.show())

"""
Shuffle : Move data from one server to another
Physical and Logical plan from spark.

Use this command for antiword dependencies
sudo apt-get install antiword

"""