import json
import requests

def main():

    europe = []

    response = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,population,region", timeout=10)
    data = response.json()
    if response.status_code == 200:

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

        europe.sort(key=lambda x: x[2], reverse=True) # sortowanie po 2+1 elemencie tupli
        print(len(europe), " krajów jest w Europie")

        print("TOP-10:")
        for i in range(0,10):
            print(f"{i+1}. {europe[i][0]} - capital: {europe[i][1]} - population: {europe[i][2]:,}")

        for i in europe:
            suma = 0
            suma = suma + int(europe[i][2])
        print(suma)

    else:
        print("Error ", response.status_code)

if __name__ == '__main__':
    main()

#https://mhyla.com/jica-python7/
