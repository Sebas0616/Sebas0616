n = float(input("Ingrese el número del cual desea saber su factorial: "))

def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)

print("El factorial de " + str(n) + " es: " + str(fact(n)))
