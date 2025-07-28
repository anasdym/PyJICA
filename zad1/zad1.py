def licz_litery(text):
   letterNumber = {}
   text = text.lower()
   result = []


   for char in text:
       if 'a' <= char <= 'z':
           letterNumber[char] = letterNumber.get(char, 0) + 1


   for letter, number in sorted(letterNumber.items()):
       print(f"{letter}: {number}")
       #
       result.append(f"{letter}: {number}")

   return result


text = input("Napisz tekst: ")
result = licz_litery(text)
