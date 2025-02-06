# n=int(input("Introduce una lista de números: "))
# def contar_digitos(n):
#     return len(str(n+1))

# resultado=contar_digitos(n)
# print(resultado)

n=int(input("Introduce una lista de números: "))
def contar_digitos(n):
    if n<10:
        return 1
    return 1 + contar_digitos(n/10)

resultado=contar_digitos(n)
print(resultado)
