

from fastapi import FastAPI
from unittest import case
import json
import requests

app = FastAPI()

@app.get("/")
def root():
   return {"message": "Hello, FastAPI!"}

@app.get("/hello")
def root(name: str = "Anonim"):
   return {"message": f"Hello, {name}"}

@app.get("/calc")
def root(op:str, x:int, y:int):

   match op:
       case "add":
           return {"result": x + y}
       case "sub":
           return {"result": x - y}
       case "mul":
           return {"result": x * y}
       case "div":
           if y != 0:
               return {"result": x / y}
           else:
               return {"error": "Dzielenie przez zero!"}
       case _:
           return {"error": "Nieznana operacja"}

@app.get("/weather")
def root(city:str):

   try:
       latlogRequest = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=<miasto>", params = {'name': city}, timeout=10)
       latlogRequest.raise_for_status()
       latlog = latlogRequest.json()

       if 'results' in latlog and latlog['results']:
           first_result = latlog['results'][0]
           latitude = first_result.get('latitude')
           longitude = first_result.get('longitude')
           #return {"latitude": latitude, "longitude": longitude}

   except Exception as err:
       return {"error": f"Wystąpił błąd przy znałezeniu miasta: {err}"}

   params = {
           'latitude': latitude,
           'longitude': longitude,
           'current_weather': 'true'
       }

   try:
       response = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=10)
       response.raise_for_status()
       data = response.json()

       if 'current_weather' in data:
           current_weather = data['current_weather']
           temperature = current_weather.get('temperature')
           windspeed = current_weather.get('windspeed')
           cloudcover = current_weather.get('cloudcover')
           time = current_weather.get('time')

           return {
               'temperature': temperature,
               'windspeed': windspeed,
               'cloudcover': cloudcover,
               'time': time,
           }

   except Exception as err:
       return {"error": f"Wystąpił błąd przy pobieraniu danych pogodowych: {err}"}

# cd ./API/
# uvicorn main:app --reload

