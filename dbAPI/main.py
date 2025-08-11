from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

conn = sqlite3.connect('animals.db', check_same_thread = False) # create file db
conn.row_factory = sqlite3.Row

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS animals (
   id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   species TEXT NOT NULL,
   age INTEGER NOT NULL,
   UNIQUE(name, species)
)
""")

class AnimalInput(BaseModel):
 name: str
 species: str
 age: int

class AnimalNameUpdate(BaseModel):
 name: str

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "API is working!"}

@app.get("/animals")
def get_animals():

   cur.execute("SELECT * FROM animals")
   list = []
   for r in cur.fetchall():
       list.append(r)
   return list


@app.get("/animals/{id}")
def get_animals(id: int):

   cur.execute("SELECT * FROM animals WHERE id = ?", (id,))
   list = []
   for r in cur.fetchall():
       if r == None:
           raise HTTPException(status_code=404, detail="Not found")
       else:
           list.append(r)
           return list


@app.put("/animals/{id}")
def update_animal_name(id: int, animal_update: AnimalNameUpdate):

    cur.execute("SELECT * FROM animals WHERE id = ?", (id,))
    existing = cur.fetchone()

    if not existing:
        raise HTTPException(status_code=404, detail="Zwierzę nie istnieje")

    cur.execute(
        "UPDATE animals SET name = ? WHERE id = ?",
        (animal_update.name, id)
    )
    conn.commit()

    # Pobierz zaktualizowany rekord
    cur.execute("SELECT * FROM animals WHERE id = ?", (id,))
    updated = cur.fetchone()

    return dict(updated)


@app.post("/animals")
def create_animal(animal: AnimalInput):

    cur.execute("SELECT * FROM animals WHERE name = ? AND species = ?", (animal.name, animal.species))
    existing = cur.fetchone()

    if existing:
        raise HTTPException(status_code=409, detail="Zwierzę już istnieje (duplikat name + species)")

    cur.execute(
        "INSERT INTO animals (name, species, age) VALUES (?, ?, ?)",
        (animal.name, animal.species, animal.age)
    )
    conn.commit()

    new_id = cur.lastrowid
    cur.execute("SELECT * FROM animals WHERE id = ?", (new_id,))
    new_animal = cur.fetchone()

    return dict(new_animal)

@app.delete("/animals/{id}")
def delete_animal(id: int):

    cur.execute("SELECT * FROM animals WHERE id = ?", (id,))
    existing = cur.fetchone()

    if not existing:
        raise HTTPException(status_code=404, detail="Zwierzę nie istnieje")

    cur.execute("DELETE FROM animals WHERE id = ?", (id,))
    conn.commit()

    return {"detail": f"Zwierzę o ID {id} zostało usunięte"}


# https://mhyla.com/jica-python10/#zadanie-animals-api-z-baz%C4%85-sqlite

# cd .\dbapi\
# uvicorn main:app --reload

















