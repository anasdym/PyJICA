#Wczytaj od użytkownika 3 komentarze tekstowe (np. opinie o zajęciach) i umieść je w liście.
# Rozbij każdy komentarz na słowa i utwórz set zawierający wszystkie unikalne słowa ze wszystkich komentarzy.
# Wypisz liczbę unikalnych słów oraz te, które mają więcej niż 5 liter.
# Jeśli wśród komentarzy pojawi się słowo „Python”, wypisz komunikat: „Uczestnicy lubią Pythona!”.

comments = []
for i in range(3):
    i = input("Podaj comentarz")
    comments.append(i)

slowa = {"Test"}
for i in comments:
    for j in i.split():
        slowa.add(j)

print(slowa)

if "Python" in slowa:
    print("Uczestnicy lubią Pythona!")



