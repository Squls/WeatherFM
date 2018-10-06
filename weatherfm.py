from gtts import gTTS
from random import *
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()

weather_api_token = os.getenv("WEATHER_KEY")
location_api_token = os.getenv("LOCATION_KEY")

def getData():
    lat = str(round(uniform(0, 181) - 90,3))
    lon = str(round(uniform(0, 361)  -180, 3))

    location_api_url = "http://api.geonames.org/findNearbyPlaceNameJSON?lat=" + lat + "&lng=" + lon + "&username=" + location_api_token
    weather_api_url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&appid=" + weather_api_token

    location_response = requests.get(location_api_url).json()
    
    if location_response['geonames']:
        town = location_response['geonames'][0]['name']
        country = location_response['geonames'][0]['countryName']

        weather_response = requests.get(weather_api_url).json()

        weather_type = weather_response['weather'][0]['main']
        temp = str(round(weather_response['main']['temp'] - 273.15,0))

        if weather_type == "Rain":
            weather = "raining"
        elif weather_type == "Sun":
            weather = "sunny"
        elif weather_type == "Clouds":
            weather = "cloudy"
        elif weather_type == "Drizzle":
            weather = "drizzling"
        elif weather_type == "Snow":
            weather = "snowing"
        elif weather_type == "Thunderstorm":
            weather = "stormy"
        else:
            weather = "clear"

        txt = "The weather at latitude " + lat + ", longitude " + lon + ", " + town + " in " + country + " is currently " + weather + ". The temperature is " + temp + " degrees centigrade"
        lng = 'en'
        obj = gTTS(text=txt, lang=lng, slow=False) 

        obj.save("report.mp3")
    else:
        getData()
        
getData()