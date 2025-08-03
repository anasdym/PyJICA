# zadanie https://mhyla.com/jica-python6/

import random
import pandas as pd

def generate(cities):

    prognoza = {
        'Miasto': [],
        'Temperatura': [],
        'Warunki': []
    }

    for city in cities:
        prognoza['Miasto'].append(city)

        temp = random.uniform(-10, 35).__round__(1)
        prognoza['Temperatura'].append(str(temp) + '°C')

        cond = ["Słonecznie", "Deszczowo", "Zachmurzenie"]
        random.shuffle(cond)
        prognoza['Warunki'].append(cond[0] )

    prognozaTab = pd.DataFrame(prognoza)
    print(prognozaTab)
    
def main ():
   cities = input("Miasta do prognozy: ")
   cities = cities.split()
   print("")
   generate(cities)

if __name__ == "__main__":
   main()