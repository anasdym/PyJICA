#Napisz program, który:
# ma zdefiniowaną tuplę z 10 wynikami egzaminów (liczby od 0 do 100),
# wypisze liczbę ocen powyżej 50,
# wypisze największy i najmniejszy wynik.

tuple = (76, 86, 35, 86, 99, 67, 44, 33, 37, 68)
liczba50 = 0

for i in tuple:
    if i > 50:
        liczba50 += 1
print(liczba50)
print(max(tuple))
print(min(tuple))

