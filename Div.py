n = int(input("Ingrese el dividendo: "))
m = int(input("Ingrese el divisor: "))

def rec(n, m):
    if(m>n):
        return 0
    elif(m==0):
        return "No se puede la división por 0"
    else:
        return rec((n-m), m)+1

def ite(n, m):
    div = 0
    if(m==0):
        return "No se puede la división por 0"
    for i in range(n):
        if((n-m)>=0):
            n -= m
            div += 1
    return div

print("División por función recursiva: " + str(rec(n, m)))
print("Potencia por función iterativa: " + str(ite(n, m)))
