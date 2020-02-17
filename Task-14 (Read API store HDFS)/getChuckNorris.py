
import json
import requests

from io import StringIO


output = StringIO()


fileWriter = open("data.json", "w+")
counter = 0
stringIO = StringIO()
while counter <= 10:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    stringIO.write(str(response.json())+"\n")
    print(str(response.json())+"\n")
    counter += 1


data = stringIO.getvalue()

fileWriter.write(data[0:len(data)])
stringIO.close()
fileWriter.close()

# fileWriter.write(str(response.json())+ "\n")

fileWriter.close()