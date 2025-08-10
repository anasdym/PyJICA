from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from unittest import case
import json
import requests

class AnimalInput(BaseModel):
   name: str
   species: str
   age: int

class AnimalNameUpdate(BaseModel):
   name: str

animals = [
   {"id": 1, "name": "Burek", "species": "dog", "age": 5},
   {"id": 2, "name": "Mruczek", "species": "cat", "age": 3},
]

app = FastAPI()

@app.get("/ping")
def ping():
   return {"status": "api is working!"}

@app.get("/animals")
def get_animals():
   return animals

@app.get("/animals/search")
def search_animals(name: str = ""):
    for animal in animals:
        if animal["name"].lower().find(name.lower()) != -1:
            return animal
    raise HTTPException(status_code=404, detail="Not found")

@app.get("/animals/{id}")
def get_animals(id: int):
    for animal in animals:
       if animal["id"] == id:
           return animal
    raise HTTPException(status_code=404, detail="Not found")

@app.put("/animals/{id}")
def update_animal_name(id: int, animal_update: AnimalNameUpdate):
    for animal in animals:
        if animal["id"] == id:
            animal.update({"name": animal_update.name})
            return animal
    raise HTTPException(status_code=404, detail="Not found")

@app.post("/animals")
def create_animal(animal: AnimalInput):
   #new_id = max(c["id"] for c in animals) + 1
   if animals:
       new_id = animals[-1]["id"] + 1
   else:
       new_id = 1
   new_animal = {
       "id": new_id,
       "name": animal.name,
       "species": animal.species,
       "age": animal.age,
   }
   animals.append(new_animal)
   return animals

@app.delete("/animals/{id}")
def delete_animal(id: int):
   for animal in animals:
       if animal["id"] == id:
           animals.remove(animal)
           return animals
   raise HTTPException(status_code=404, detail="Not found")

# cd .\app\
# uvicorn main:app --reload

