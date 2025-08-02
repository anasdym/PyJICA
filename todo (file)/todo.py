# zadanie https://mhyla.com/jica-python6/
from operator import indexOf

zadania = {}

def dodaj_zadanie():
   global zadanie
   tytul = input("Napisz tytuł zadania: ")
   priorytet = input("Napisz priorytet zadania: ")
   zadanie = (tytul, priorytet)
   zadania[zadanie] = False

def pokaz_zadania():
   for i, status in zadania.items():
       if status:
           print(indexOf(zadania, i) + i, " [✔]")
       else:
           print(indexOf(zadania, i) + i," [ ]")

while True:
    dodaj_zadanie()

    komenda = input("\nChcesz..\ndodać kolejne? - napisz TAK\noznaczyć jako wykonane - napisz ZROB\nusunąć zadanie? - napisz USUŃ")
    komenda = komenda.lower()
    match komenda:
        case "tak":
            dodaj_zadanie()
        case "zrob":
            pokaz_zadania()

        case "usuń":
            pokaz_zadania()

        case _:
            pokaz_zadania()
            break
