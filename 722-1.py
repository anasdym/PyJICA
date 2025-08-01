# Napisz program, który od użytkownika przyjmie liczbę (1-50),
# a następnie wydrukuje tyle znaków # ile podał użytkownik

i  = 1
liczba  = int(input("podaj liczbe #"))
if liczba >= 1 and liczba <=50:
    while i <= liczba:
        i += 1
        print('#')