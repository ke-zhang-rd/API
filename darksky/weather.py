import json
import pprint
import requests
import time
now = time.time()
#url = "https://api.darksky.net/forecast/fs735892ewqerasdfefasdfef98dfe/40.866610,-72.881760"
#text = requests.get(url.format(api_key='fs735892ewqerasdfefasdfef98dfe', lat=0, long=0, time=int(now))).text
url = "https://api.darksky.net/forecast/{YOUR_SECREATE_KEY}/40.866610,-72.881760"
text = requests.get(url.format(api_key='{YOUR_SECREATE_KEY}', lat=0, long=0, time=int(now))).text
data = json.loads(text)

pprint.pprint(data['currently']['apparentTemperature'])
