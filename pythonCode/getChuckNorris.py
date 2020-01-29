import json
import requests

fileWriter = open("data.json", "w+")
counter = 0
while counter <= 10:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    fileWriter.write(str(response.json())+ "\n")
    counter += 1
    print("Working")

fileWriter.close()