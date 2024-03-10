#ejercicio 9 sem_03 - 04

def elemento_central(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if matriz else 0

    if filas % 2 == 1 and columnas % 2 == 1:
        fila_central = filas // 2
        columna_central = columnas // 2
        return matriz[fila_central][columna_central]
    else:
        return "La matriz no tiene un solo elemento central."

matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento = elemento_central(matriz_ejemplo)
print( elemento)