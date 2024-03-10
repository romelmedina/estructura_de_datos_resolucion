#ejercicio 4 sem_03 - 04

def imprimir_piramide_invertida(n):
    if n <= 0:
        return
    imprimir_piramide_invertida_row(n)
    imprimir_piramide_invertida(n - 1)

def imprimir_piramide_invertida_row(row_number):
    if row_number == 0:
        return
    else:
        print(row_number, end=" ")
        imprimir_piramide_invertida_row(row_number - 1)

n = int(input("Ingrese un número para la pirámide de números invertidos: "))
imprimir_piramide_invertida(n)