import json
import requests

europe = []

def getData():
    try:
        response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,population,region", timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.ConnectionError as err:
        print(f"Brak internetu: {err}")

    except json.JSONDecodeError:
        print("Bład: puste odpowiedzi z api-pogoda.")

def main():

    data = getData()

    for country in data:
        if country["region"] == "Europe":
            name = country["name"]["common"]
            if country["capital"]:
                capital = country["capital"][0]
            else:
                capital = "-"

            population = country["population"]

            tuple = (name, capital, population)
            europe.append((tuple))
    europe.sort(key=lambda x: x[2], reverse=True)  # sortowanie po 2+1 elemencie tupli
    print(len(europe), " krajów jest w Europie")
    print("\nTOP-10 of population:")
    for i in range(0, 10):
        print(f"{i + 1}. {europe[i][0]} - capital: {europe[i][1]} - population: {europe[i][2]:,}") # {:,} - 1,000
    europePop = sum(item[2] for item in europe)
    print(f"\nSuma populacji wszystkich krajów w europe: {europePop:,}")

if __name__ == '__main__':
    main()

#https://mhyla.com/jica-python7/
