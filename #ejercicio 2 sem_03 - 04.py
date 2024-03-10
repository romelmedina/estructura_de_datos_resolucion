#ejercicio 2 sem_03 - 04

def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        suma_anterior = suma_recursiva(n - 1)
        suma_actual = suma_anterior + n
        return suma_actual

n = int(input("Ingrese un número para calcular la suma de los números del 1 al n: "))
resultado = suma_recursiva(n)
print( n,  resultado)