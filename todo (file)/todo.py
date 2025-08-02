zadania = {}

def dodaj_zadanie():
    global zadanie
    tytul = input("Napisz tytuł zadania: ")
    priorytet = input("Napisz priorytet zadania: ")
    zadanie = (tytul, priorytet)
    zadania[zadanie] = False

def pokaz_zadania():
    for i, (zadanie, status) in enumerate(zadania.items()): #wraca z numerem slownika
        if status:
            print(f"{i + 1}. {zadanie} [✔]")
        else:
            print(f"{i + 1}. {zadanie} [ ]")

def wykonaj_zadanie():
    n = int(input("Które zadanie jest już wykonane? - napisz numer"))
    #zaprogramowac oznaczenie
    pokaz_zadania()

def usun_zadanie():
    n = int(input("Które zadanie usunąć? - napisz numer"))
    # zaprogramowac usuwanie
    pokaz_zadania()

def main ():
        dodaj_zadanie()

        while True:
            komenda = input("\nChcesz..\ndodać kolejne? - napisz TAK\noznaczyć jako wykonane - napisz ZROB\nusunąć zadanie? - napisz USUN")
            komenda = komenda.lower()

            match komenda:
                case "tak":
                    dodaj_zadanie()
                case "zrob":
                    pokaz_zadania()
                    wykonaj_zadanie()
                case "usun":
                    pokaz_zadania()
                    usun_zadanie()
                case _:
                    pokaz_zadania()
                    break

if __name__ == "__main__":
   main()

# zadanie https://mhyla.com/jica-python6/