# Napisz program, który:
# zapyta użytkownika o liczbę N,
# wypisze wszystkie liczby od 1 do N w jednej linii, używając pętli while.

i  = 1
liczba = int(input("podaj liczbe N: "))
if liczba >= 1:
    while i <= liczba:
        print(i, end=" ")
        i += 1
