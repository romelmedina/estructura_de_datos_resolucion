#ejercicio 1 sem_03 - 04

def imprimir_pares(n):
    if n <= 0:
        return
    imprimir_pares(n - 1)
    if n % 2 == 0:
        print(n)

imprimir_pares(100)