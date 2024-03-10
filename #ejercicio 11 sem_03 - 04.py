#ejercicio 11 sem_03 - 04

def multiplicar_matriz_por_numero(matriz, numero):
    filas = len(matriz)
    columnas = len(matriz[0])

    matriz_resultado = [[0] * columnas for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            matriz_resultado[i][j] = matriz[i][j] * numero

    return matriz_resultado

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = float(input("Ingrese el número escalar para multiplicar la matriz: "))

resultado = multiplicar_matriz_por_numero(matriz, escalar)
