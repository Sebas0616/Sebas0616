c = 0
i = 1
n = 2
lista = []
suma = 0

while i<n:
    if i%2 == 0:
        ##print(i, end = " ")
        lista.append(i)
        c = c + 1
    if c == 20:
        n = 0
    i += 1
    n += 1

for j in lista:
    suma = suma + j
print("La suma de los primero 20 números pares es: " + str(suma))
