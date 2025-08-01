# Napisz program, który:
# losuje liczbę od 1 do 10,
# prosi użytkownika o zgadywanie liczby, aż zgadnie,
# wyświetla komunikat: „Za mało” lub „Za dużo”, a po trafieniu: „Brawo!”.
import random as r

a = r.randint(1,10)

#liczba  = int(input("Zgadnij liczbe od 1 do 10: "))

#if i == liczba:
#    print("Brawo!")
#else:
#    if i > liczba:
#        print("Za mało")
#    else:
#    print(a)

while True:
    b = int(input("Zgadnij liczbe od 1 do 10: "))
    if a > b:
        print("Za mało")
    if a < b:
        print("Za dużo")
    if a == b:
        print("Brawo!")
        break


