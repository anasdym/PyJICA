#Ma zdefiniowaną tuplę 10 dostępnych produktów w sklepie, np.:
# Poprosi użytkownika o dodanie 3 produktów do koszyka (wczytaj z input() i dodaj do listy koszyk).
# Sprawdzi, czy każdy wybrany produkt znajduje się w ofercie sklepu. Jeśli nie, wypisze komunikat:
# „Produkt X jest niedostępny”.
# Na koniec wypisze wszystkie produkty w koszyku, uporządkowane alfabetycznie.

produkty = ("mleko", "chleb", "masło", "ser", "jabłka")
produtyList = list(produkty)

koszyk = []
print("Dodaj 3 produkty do koszyka: ")
for i in range(1,4):
    nowy = input()

    if produtyList.count(nowy) == 0:
        print("Produkt", nowy, "jest niedostępny")

    koszyk.append(nowy)

koszyk.sort()
print ("Koszyk:", koszyk)

