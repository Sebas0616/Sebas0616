n = int(input("Ingrese el número del incio del rango: "))
m = int(input("Ingrese el número del final del rango: "))
c = 0
for i in range(n, m+1):
    c = c + i
print("La suma de los números comprendidos entre " + str(n) + " y " + str(m) + " es: " + str(c))
