import requests
import json

url = 'http://wwww.cbr-xml-daily.ru/daily_json.js'
respond = requests.get(url)
data = json.loads(respond.text)
print(data)