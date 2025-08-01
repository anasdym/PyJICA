zdanie = input("Podaj zdanie: ")
slowa = zdanie.split()
slownik_wystapien = {}

for slowo in slowa:
    slowo = slowo.lower()
    if slowo in slownik_wystapien:
        slownik_wystapien[slowo] += 1
    else:
        slownik_wystapien[slowo] = 1

wystapienia = dict(sorted(slownik_wystapien.items()))
print(wystapienia)