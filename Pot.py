n = int(input("Ingrese la base: "))
m = int(input("Ingrese la potencia: "))

def rec(n, m):
    if(m==0):
        return 1
    elif(m==1):
        return n
    else:
        return rec(n, m-1)*n

def ite(n, m):
    pot = n
    for i in range(m-1):
        pot *= n
    return pot

print("Potencia por función recursiva: " + str(rec(n, m)))
print("Potencia por función iterativa: " + str(ite(n, m)))
