import requests
from fastapi import FastAPI

def get_animals():
   response = requests.get("http://127.0.0.1:8000/animals")
   print(response.json)

def add_animal():
   animal = {
       "name": "Borys",
       "species": "cat",
       "age": 4,
   }

   response = requests.post("http://127.0.0.1:8000/animals", json=animal)
   print("- zwierzątko dodane -")
   print(response.json())

def delete_animal():
   response = requests.delete("http://127.0.0.1:8000/animals/1", json={"id": 1})
   print("- zwierzątko usunięte -")
   print(response.json())

def main():
   get_animals()
   add_animal()
   delete_animal()

if __name__ == "__main__":
   main()

