#ejercicio 3 sem_12 - 13

from collections import deque

def bfs_laberinto(laberinto, inicio, destino):
    filas = len(laberinto)
    columnas = len(laberinto[0])

    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    cola = deque([(inicio, [inicio])])

    while cola:
        (fila, columna), camino = cola.popleft()

        if (fila, columna) == destino:
            return camino

        for df, dc in direcciones:
            nueva_fila, nueva_columna = fila + df, columna + dc

            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] != 1:
                cola.append(((nueva_fila, nueva_columna), camino + [(nueva_fila, nueva_columna)]))
                laberinto[nueva_fila][nueva_columna] = 1
    return None

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]
inicio = (0, 0)  
destino = (4, 4)  

camino_mas_corto = bfs_laberinto(laberinto, inicio, destino)
if camino_mas_corto:
    print (camino_mas_corto)
else:
    print("No se encontró un camino al destino.")
