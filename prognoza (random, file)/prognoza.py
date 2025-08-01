# zadanie https://mhyla.com/jica-python6/

import random

def generate(cities):
    
    temps = []
    tempsCity = {}
    raport = []
    
    raport.append("- prognoza podody - ")
    
    for city in cities:
        temp = random.randint(-10, 35)
        cond = ["Słonecznie", "Deszczowo", "Zachmurzenie"]
        random.shuffle(cond)
        
        raport.append(f"Miasto: {city}. Temperatura: {temp}°C. Warunki: {cond[0]}.")
       
       #---analiza--
        temps.append(temp)
        tempsCity[city] = temp
    
    temp_ave = round(sum(temps) / len(temps), 1)
    
    temp_max = max(temps)
    city_max = [city for city, temp in tempsCity.items() if temp == temp_max][0]
    
    temp_min = min(temps)
    city_min = [city for city, temp in tempsCity.items() if temp == temp_min][0]
    
    results = f"- analiza - \nSrednia temperatura: {temp_ave}°C. Maksymalna ({temp_max}°C) jest w {city_max}, a minimalna ({temp_min}°C) w {city_min}."
    #---   
       
    raport.append(results)
    
    #---saving to file & ---
    with open("raport.txt", "a") as f:
        for i in raport:
            f.write(i)
            print(i)
        print("- zapisano do raport.txt -")
    
def main ():
   cities = input("- napisz listę miast do prognozy -\n")
   cities = cities.split()
   generate(cities)

if __name__ == "__main__":
   main()



