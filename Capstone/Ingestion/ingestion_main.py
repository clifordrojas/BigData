import json
import subprocess
import requests
import sys

def read_neobi_weed(key):
    url = "https://neobi.p.rapidapi.com/api/products"
    querystring = {"count":"250","htmlDescription":"false","sort":"created","page":"1","rev":"v1.6"}
    headers = {
        'x-rapidapi-host': "neobi.p.rapidapi.com",
        'x-rapidapi-key': key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response

def read_neobi_producer(key):
    url = "https://neobi.p.rapidapi.com/api/producers"

    querystring = {"count": "250", "page": "1", "rev": "v1.6"}

    headers = {
        'x-rapidapi-host': "neobi.p.rapidapi.com",
        'x-rapidapi-key': key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

def read_file_json(file_name):
    with open(file_name+".json") as f:
        json_data = json.load(f)
        return json_data

def create_local_weed(data):
    with open("neobi_api_weed.json", "w") as local_file:
        json.dump(data,local_file)

def create_local_file_producer(data):
    with open("neobi_api_producer.json", "w") as local_file:
        json.dump(data,local_file)



if __name__ == '__main__':
    key = sys.argv[1]
    print(key)
    data = read_neobi_weed(key)
    json_data = json.loads(data.text)
    create_local_weed(json_data)

    # data = read_neobi_producer(key)
    # json_data = json.loads(data.text)
    # create_local_file_producer(json_data)

    # bash_command = 'hadoop fs -copyFromLocal neobi_api_producer.json /data'
    # process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    # output, error = process.communicate()



    # file_name = "neobi_api"
    # data = read_file_json(file_name)



