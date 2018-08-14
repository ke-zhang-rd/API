import json
import pprint
import requests
import time
now = time.time()
url = "https://api.darksky.net/forecast/b63d08d301bdd01da4c4f1218610372f/40.866610,-72.881760"
text = requests.get(url.format(api_key='b63d08d301bdd01da4c4f1218610372f', lat=0, long=0, time=int(now))).text
data = json.loads(text)

pprint.pprint(data['currently']['apparentTemperature'])
