#ejercicio 15 sem_03 - 04

def encontrar_maximo(matriz):
    maximo = matriz[0][0]

    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento

    return maximo

matriz = [
    [1, 2, 3],
    [4, 9, 6],
    [7, 8, 5]
]

maximo = encontrar_maximo(matriz)

print( maximo)