def factorial ():
    n=int(input("Introduzca un número: "))
    resultado=1
    for i in range (2, n+1):
            resultado*=i
    return resultado

r=factorial()
print(r)