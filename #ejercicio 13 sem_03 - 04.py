#ejercicio 13 sem_03 - 04


import random

def crear_matriz_aleatoria(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(0, 100) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

filas = 100
columnas = 100

matriz_aleatoria = crear_matriz_aleatoria(filas, columnas)

print("Matriz de números aleatorios:")
for fila in matriz_aleatoria:
    print(fila)