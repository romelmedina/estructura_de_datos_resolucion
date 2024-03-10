#ejercicio 8 sem_03 - 04

def crear_matriz_de_matrices(m, n):
    matriz = []
    for i in range(m):
        fila = []
        for j in range(n):
            matriz_interna = []
            for k in range(int(input(f"Ingrese el número de elementos para la matriz interna [{i}][{j}]: "))):
                elemento = input(f"Ingrese el elemento {k+1} de la matriz interna [{i}][{j}]: ")
                matriz_interna.append(elemento)
            fila.append(matriz_interna)
        matriz.append(fila)
    return matriz
filas = int(input("Ingrese el número de filas de la matriz de matrices: "))
columnas = int(input("Ingrese el número de columnas de la matriz de matrices: "))

matriz_de_matrices = crear_matriz_de_matrices(filas, columnas)

print("La matriz de matrices creada es:")
for fila in matriz_de_matrices:
    print(fila)