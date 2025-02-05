def potencia(a, b):
    if b==0:
        return 1
    elif b==1:
        return a
    return a*potencia(a, b-1)

a=int(input("Introduce un número base: "))
b=int(input("Introduce un exponente: "))
resultado=potencia(a, b)
print(resultado)