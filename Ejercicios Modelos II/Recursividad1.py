n = int(input("Ingrese la base: "))
m = int(input("Ingrese la potencia: "))

def pot(n, m):
    if(m==0):
        return 1
    elif(m==1):
        return n
    else:
        return pot(n, m-1)*n

print(str(n) + " elevado a la " + str(m) + " es: " + str(pot(n, m)))
