#ejercicio 3 sem_03 - 04

def imprimir_piramide(n, current_row=1):
    if current_row > n:
        return
    else:
        imprimir_piramide_row(current_row)
        imprimir_piramide(n, current_row + 1)

def imprimir_piramide_row(row_number):
    if row_number == 0:
        return
    else:
        imprimir_piramide_row(row_number - 1)
        print(row_number, end=" ")
        
n = int(input("Ingrese un número para la pirámide de números: "))
imprimir_piramide(n)