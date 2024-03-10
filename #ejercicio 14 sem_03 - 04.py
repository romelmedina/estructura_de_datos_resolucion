#ejercicio 14 sem_03 - 04

import numpy as np
import statistics

def calcular_estadisticas_matriz(matriz):
    elementos = [elemento for fila in matriz for elemento in fila]

    media = np.mean(elementos)

    mediana = np.median(elementos)

    desviacion_estandar = np.std(elementos)

    return media, mediana, desviacion_estandar

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

media, mediana, desviacion_estandar = calcular_estadisticas_matriz(matriz)

print( media)
print( mediana)
print( desviacion_estandar)