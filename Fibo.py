n = int(input("Ingrese límite de la sucesión: "))

def rec(n):
    if(n<=2):
        return 1
    else:
        return rec(n-1)+rec(n-2)

def ite(n):
    a, b, fib = 0, 1, 1
    for i in range(1, n):
        fib += a
        a, b = b, fib
    return fib

print("Fibonacci por función recursiva: " + str(rec(n)))
print("Fibonacci por función iterativa: " + str(ite(n)))
