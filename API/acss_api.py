import requests
import pandas
import json

url = 'https://pokeapi.co/api/v2/pokemon/ditto'

respon = requests.get(url)
data = respon.json()
datadump = json.dumps(data,indent=4)
print (datadump)