# zadanie https://mhyla.com/jica-python6/

zadania = []

def dodaj_zadanie():
   global zadanie
   tytul = input("Napisz tytuł zadania: ")
   priorytet = input("Napisz priorytet zadania: ")
   zadanie = (tytul, priorytet)
   zadania.append(zadanie)


def pokaz_zadania():
   for i in zadania:
       print(i)


while True:
   dodaj_zadanie()


   kolejne = input("Chcesz dodać kolejne? ")
   if kolejne.lower() != "tak":
       pokaz_zadania()
       break

