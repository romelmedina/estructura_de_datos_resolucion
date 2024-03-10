#ejercicio 6 sem_03 - 04

def crear_matriz(m, n):
    matriz = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(float(input(f"Ingrese el elemento en la posición [{i}][{j}]: ")))
        matriz.append(fila)
    return matriz

filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

matriz = crear_matriz(filas, columnas)

print("La matriz creada es:")
for fila in matriz:
    print(fila)