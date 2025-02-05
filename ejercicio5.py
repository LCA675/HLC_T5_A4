# n=int(input("Introduce una lista de números: "))
# def contar_digitos(n):
#     return len(str(n+1))

# resultado=contar_digitos(n)
# print(resultado)

n=int(input("Introduce una lista de números: "))
def contar_digitos(n):
    resto=0
    contador=0
    if n==0:
        return 0
    else:
        resto=n/10
        contador+=contador
    return contador


resultado=contar_digitos(n)
print(resultado)
