#Napisz program, który przechodzi przez liczby od 1 do 20 i dla każdej liczby:
# wypisuje „parzysta”, jeśli liczba jest parzysta,
# wypisuje „nieparzysta”, jeśli liczba jest nieparzysta.

for i in range(1, 21):
    if i % 2 == 0:
        print(i, "parzyste")
    else:
        print(i, "nieparzyste")