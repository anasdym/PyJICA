print("wiek")
wiek = int(input())
#student = input("student?")

#dzien = int(input("dzien?"))

#if student == "tak":
   # //student = True
   # //kwota = 20
kwota = 45

if wiek <= 3 or wiek >= 70:
    kwota = 0
elif wiek < 26:
    kwota = 35

print(kwota, "zl")

