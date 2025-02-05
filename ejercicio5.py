n=int(input("Introduce una lista de números: "))
def contar_digitos(n):
    return len(str(n+1))

resultado=contar_digitos(n)
print(resultado)