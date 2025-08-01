#Napisz program, który:
# wczyta od użytkownika 5 ocen (liczb całkowitych)
# i zapisze je do listy, obliczy średnią ocen,
# wypisze komunikat „Zaliczone”,
# jeśli średnia jest większa lub równa 3.0, w przeciwnym razie „Nie zaliczone”.

oceny = []
print("Wpisz 5 ocen: ")
for i in range(1,6):
    oceny.append(input())

sred = 0
for i in range(0, 5):
    sred += int(oceny[i]) / 5

if sred > 3:
    print("Zaliczone")
else:
    print("Nie zaliczone")







