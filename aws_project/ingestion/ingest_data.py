import json
import requests
from io import StringIO
import boto3
s3 = boto3.client("s3")
output = StringIO()


fileWriter = open("data.json", "w+")
counter = 0
stringIO = StringIO()
while counter <= 5:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    stringIO.write(str(response.json())+"\n")
    print(str(response.json())+"\n")
    counter += 1


data = stringIO.getvalue()

#fileWriter.write(data[0:len(data)])
s3.put_object(Bucket = "2020clifordrojas", Key = "All_the_Jokes.txt", Body = data[0:len(data)])
stringIO.close()
fileWriter.close()
# fileWriter.write(str(response.json())+ "\n")
fileWriter.close()