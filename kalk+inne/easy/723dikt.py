person = {
    "eyes": "blue",
    "hair": "dark-blonde",
    "skin": "pale",
    "height": "169",
    "weight": "67",
    "figure": "skinny fat",
    "age": "28"
}

dog = {
    "type": "spaniel",
    "color": "white"
}

#phone = {
    #"model": "Samsung"
#}

person.update({"type": 1})
print(person)

print(person)

ana = person.copy()
print(ana)

colors = dict.fromkeys(['eyes', 'hair'], "incredible")
print(colors)

print(person.get('age', 'brak'))

print(person.items())

print(person.keys())

person.pop('figure')
print(person)

person.popitem()
print(person)

person.setdefault('status', 'married')
print(person)



person.clear()
print(person.values())