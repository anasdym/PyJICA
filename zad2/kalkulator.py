def add(a, b):
   return a + b
def sub(a, b):
   return a - b
def mul(a, b):
   return a * b
def div(a, b):
   return a / b
def pow(a, b):
   return a ** b

result = []
history = []

def main ():
    pobierz_wejscie()


def pobierz_wejscie():
    while True:
        user_input = input().lower()

        match user_input:

            case 'exit' | 'quit':
                break

            case 'history':
                for each in history:
                    print(each)

            case 'clear':
                history.clear()

            case _:
                wykonaj_operacje(user_input)

        # if user_input in ['exit', 'quit']:
        #     break
        # elif user_input == 'history':
        #     for each in history:
        #         print(each)
        # else:
        #     wykonaj_operacje(user_input)


def wykonaj_operacje(user_input):
    try:
        part = user_input.split()
        param0 = float(part[0])
        sign = part[1]
        param1 = float(part[2])

        match sign:
            case '+':
                result = add(param0, param1)
            case '-':
                result = sub(param0, param1)
            case '*':
                result = mul(param0, param1)
            case '/':
                result = div(param0, param1)
            case '^':
                result = pow(param0, param1)
            case _:
                raise ValueError("zly typ dzialania")

        print(result)
        history.append(f"{user_input} = {result}")

    except ZeroDivisionError:
        print("Nie wolno dzielic przez 0")

    except ValueError as e:
        print("Bledna wartosc: " + str(e))

    except:
        print("Shit happend")

if __name__ == '__main__':
   main()


