
wyniki = (45, 67, 82, 90, 55, 74, 100, 61)
wynikiList = list(wyniki)

#Policz i wypisz średnią ocen.
sred = 0
for i in range(0, 8):
    sred += wynikiList[i]
sred = sred / 8
print("Srednia ocen:", sred, "\nWyniki wyzej sredniej: ")

# Wypisz wszystkie wyniki powyżej średniej.
# Wypisz ile osób zdało test (wynik >= 60).
# Jeśli ktoś zdobył 100 punktów, wypisz komunikat:
# „Gratulacje dla najlepszego uczestnika!”.

osoby60 = 0;

for i in range(0, 8):
    if wynikiList[i] > sred:
        print(wynikiList[i])
    if wynikiList[i] == 100:
        print("Gratulacje dla najlepszego uczestnika!")
    if wynikiList[i] >= 60:
        osoby60 += 1
print("Zdało test ", osoby60, "osoby")


