lista = []
suma = 0

for i in range(5):
    n = int(input("Ingrese un número: "))
    lista.append(n)

for i in lista:
    suma = suma + i

media = suma/5
print("La media aritmetica de la lista es: " + str(media))
