zadania = {}

def dodaj_zadanie():
    tytul = input("Napisz tytuł zadania: ")
    priorytet = input("Napisz priorytet zadania: ")
    zadanie = (tytul, priorytet)
    zadania[zadanie] = "[ ]"
    print("- zapisano! - ")

def pokaz_zadania():
    for i, (zadanie, status) in enumerate(zadania.items()): #нумерує dict
        print(f"{i + 1}. {zadanie} {status}")

def wykonaj_zadanie():
    n = int(input("Które zadanie chcesz oznaczyć? - napisz numer: "))
    for i, [zadanie, _] in enumerate(zadania.items()):
        if n == i + 1:
            zadania[zadanie] = "[✔]"
    print("- wykonane! - ")

def usun_zadanie():
    zadanie_usun = 0
    n = int(input("Które zadanie usunąć? - napisz numer: "))
    for i, [zadanie, _] in enumerate(zadania.items()):
        if i == n - 1:
            zadanie_usun = zadanie
    zadania.pop(zadanie_usun)
    print("- usunięte! - ")

def zapisz_plik():
    pokaz_zadania()
    with open("todo-history.txt", "a", encoding='utf-8') as f:
        for i, [zadanie, status] in enumerate(zadania.items()):
            f.write(f"{i + 1}. {zadanie} {status}\n")
    print("- zapisano do todo-history.txt -")

def main ():

    dodaj_zadanie()

    while True:
        komenda = input("\nChcesz..\n..dodać zadanie? - napisz DODAJ\n..oznaczyć jako wykonane? - napisz ZROB\n..usunąć zadanie? - napisz USUN\n..pokazać wszyskie? - napisz LISTA\n..zapisać do pliku? - napisz SAVE\n..zakonczyć? - napisz EXIT\n")
        komenda = komenda.lower()

        match komenda:
            case "dodaj":
                dodaj_zadanie()
            case "zrob":
                pokaz_zadania()
                wykonaj_zadanie()
            case "usun":
                pokaz_zadania()
                usun_zadanie()
            case "lista":
                pokaz_zadania()
            case "save":
                zapisz_plik()
            case "exit":
                break
            case _:
                print("Nie poprawna komenda, spobój jeszcze raz\n")

if __name__ == "__main__":
   main()

# zadanie https://mhyla.com/jica-python6/