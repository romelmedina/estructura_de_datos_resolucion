#ejercicio 16 sem_03 - 04

def encontrar_submatriz_max_suma(matriz):
    max_suma = float('-inf')
    submatriz = []

    filas = len(matriz)
    columnas = len(matriz[0])

    for fila_inicio in range(filas):
        temp = [0] * columnas
        for fila_fin in range(fila_inicio, filas):
            for i in range(columnas):
                temp[i] += matriz[fila_fin][i]
            suma, _, _ = kadane(temp)
            if suma > max_suma:
                max_suma = suma
                submatriz = [fila_inicio, _, fila_fin, _]

    return max_suma, submatriz
matriz = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

suma_maxima, submatriz = encontrar_submatriz_max_suma(matriz)

print( suma_maxima)
print( submatriz[0],  submatriz[1], submatriz[2], submatriz[3])