#ejercicio 12 sem_03 - 04

def calcular_media_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    suma_total = 0

    total_elementos = filas * columnas

    for fila in matriz:
        for elemento in fila:
            suma_total += elemento

    media = suma_total / total_elementos

    return media

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

media = calcular_media_matriz(matriz)

print( media)