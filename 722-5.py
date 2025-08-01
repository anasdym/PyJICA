#Napisz program, który wypisze kwadraty wszystkich liczb od 1 do 10

for j in range(2, 11): #10 + 1
    for i in range(1, 11):
        print(i, "^", j, "=", i**j)