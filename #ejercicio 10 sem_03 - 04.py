#ejercicio 10 sem_03 - 04

def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return "Las matrices no tienen las mismas dimensiones y no se pueden sumar."
    
    filas = len(matriz1)
    columnas = len(matriz1[0])

    matriz_resultado = [[0] * columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return matriz_resultado

matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6, 7],
    [8, 9, 10]
]

resultado = sumar_matrices(matriz1, matriz2)

print("La suma de las matrices es:")
for fila in resultado:
    print(fila)