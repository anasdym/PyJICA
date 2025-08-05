import json
from logging import exception
import requests
from requests import Response

def getCoord(city):

    try:
        response = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=<miasto>", params = {'name': city}, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'results' in data and data['results']:
            first_result = data['results'][0]
            latitude = first_result.get('latitude')
            longitude = first_result.get('longitude')
            return latitude, longitude

    except Exception as err:
        print(f'Wystąpił błąd: {err}')

def getWheather(latitude, longitude):

    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current_weather': 'true'
    }

    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast", params = params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if 'current_weather' in data:
            current_weather = data['current_weather']
            temperature = current_weather.get('temperature')
            windspeed = current_weather.get('windspeed')

            return temperature, windspeed

    except Exception as err:
        print(f'Wystąpił błąd: {err}')

def getCities():

    user_data = input("Prosze o podanie miast w jednej linii, oddzielonych przecinkami\n")
    user_cities = user_data.split(',')

    cities = []
    for i in user_cities:
        city = i.strip()
        if city:
            cities.append(city)

    if not cities:
        print("Bład: miasta nie czytelne")
        return None
    else:
        return cities

def main():

    cities = getCities()

    for city in cities:
        city_coord = getCoord(city)
        if city_coord:
            latitude, longitude = city_coord
            print(city, latitude, longitude)

            city_temp, city_wind = getWheather(latitude, longitude)
            if city_temp:
                print(f"{city_temp}°C, {city_wind} km/h")
            else:
                print(f"[WARN] Brak danych pogodowych: {city}")
        else:
            print(f"[WARN] Nie znaleziono miasta: {city}")

if __name__ == '__main__':
    main()

# https://mhyla.com/jica-python7/#mini-projekt-pogoda-dla-listy-miast--plan-krok%C3%B3w-z-wymaganiami
