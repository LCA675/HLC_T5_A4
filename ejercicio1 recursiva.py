n=int(input("Introduzca un número: "))
def factorial (n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

r=factorial(n)
print(r)