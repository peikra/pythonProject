import requests
import json


key = '18245008a4da148fd7ee0f3a35c5ab6c'

url  = 'https://api.openweathermap.org/data/2.5/onecall'
latitude = 41.7151
longitude = 44.8271
exclude = 'current'
payload = {'lat' : latitude, 'lon' : longitude, 'exclude' : exclude, 'appid': key, 'units' : 'metric'}
r = requests.get(url,params=payload)
print(r.status_code)
print(r.headers)
print(r)
print(url)
print(r.text)
result = json.loads(r.text)
temperature = print("ტემპერატურა:", result['hourly'][2]['temp'],"C")
humidity = print("ტენიანობა:", result['hourly'][2]['humidity'],"%")
windspeed = print("ქარის სიჩქარე:", result['hourly'][2]['wind_speed'])
timezone = print("ქალაქი:", result['timezone'])


with open('data.json','w') as file:
    json.dump(result,file,indent=4)


import sqlite3
conn = sqlite3.connect("weather.sqlite")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE weather 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
city VARCHAR(30),
temperature FLOAT,
humidity FLOAT,
wind_speed FLOAT);


''')
temp=( result['hourly'][2]['temp'])
hum=( result['hourly'][2]['humidity'])
wind = (result['hourly'][2]['wind_speed'])
city = ( result['timezone'])


cursor.execute("INSERT INTO weather (city,temperature,humidity,wind_speed) VALUES (?,?,?,?)",(city,temp,hum,wind))
conn.commit()
conn.close()
#შევქმენი ცხრილი სადაც მოცემული იქნება აიდი, ქალქის დასახელება, ტემპერატურა, ტენიანობა და ქარის სიჩქარე. თითოეული
#ეს მონაცემი ინსერტის საშუალებით დაემატება ცხრილში.







