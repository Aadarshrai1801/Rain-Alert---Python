# API Keys, Authentication in Python

import requests

API_KEY = "686ab37f6f0e4bb184f103e0206e3b07"
MY_LAT = 31.633980
MY_LNG = 74.872261 

parameter = {
    "lat" : MY_LAT,
    "lon" : MY_LNG,
    "exclude" : "current,minutely,daily",
    "appid" : API_KEY,
}

responses = requests.get(url = "https://api.openweathermap.org/data/2.5/onecall", params = parameter)

responses.raise_for_status()
weather_data = responses.json()

for i in range(0, 11) :
    hour_data = weather_data["hourly"][i]["weather"][0]["id"]
    
    if int(hour_data) < 700 :
        print("Bring your umbrella!")