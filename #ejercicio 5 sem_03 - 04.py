#ejercicio 5 sem_03 - 04

def imprimir_tabla_multiplicar(n, multiplicador=1):
    if multiplicador > 10:
        return
    else:
        print(f"{n} x {multiplicador} = {n * multiplicador}")
        imprimir_tabla_multiplicar(n, multiplicador + 1)

n = int(input("Ingrese un número para imprimir su tabla de multiplicar: "))
imprimir_tabla_multiplicar(n)