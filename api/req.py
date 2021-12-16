# Api is the way of communication between two programs
# Talk to the server (serves data)

# Exchange data through api



import requests
import json
response = requests.get('http://api.open-notify.org/astros.json')
# get() sends a request to the server specified in the argument
# and receives the data sent by the server in response to our request

# JSON -> JavaScript Object Notation
# Objects in js are exactly same as dictionaries in python
# myDict = {
# 	"key": "value",
# 	"blah": "blah"
# }
# When we enclose dictionry in a string, it becomes json
# Language of the api is json

# Interconversion from json to dictionary

# json.loads('json file') -> python dictionary
# json.dumps(pydict, indent=4) -> json file



data_dictionary = json.loads(response.text) # response.text is the json file
print(data_dictionary)

weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Agra&appid=d9b40f8f7249d3aa1da723782d44d61d')
# weather is a json object
weth_json = json.loads(weather.text, indent=4) # text variable stores the json file. Dot operater
print(weth_json)