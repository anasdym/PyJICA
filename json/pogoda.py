import json
from logging import exception
import requests
from requests import Response

def getData(city):

    response = response = requests.get("https://geocoding-api.open-meteo.com/v1/search?name=<miasto>", {'name': city}, timeout=10)
    response.raise_for_status()
    data = response.json()

    if 'results' in data and data['results']:
        first_result = data['results'][0]
        latitude = first_result.get('latitude')
        longitude = first_result.get('longitude')
        return latitude, longitude

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
        cityData = getData(city)
        if cityData:
            latitude, longitude = cityData
            print(city, latitude, longitude)
        else:
            print(f"[WARN] Nie znaleziono miasta: {city}")

if __name__ == '__main__':
    main()

# https://mhyla.com/jica-python7/#mini-projekt-pogoda-dla-listy-miast--plan-krok%C3%B3w-z-wymaganiami
