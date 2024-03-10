#ejercicio 7 sem_03 - 04

def crear_matriz_compleja(m, n):
    matriz = []
    for i in range(m):
        fila = []
        for j in range(n):
            real = float(input(f"Ingrese la parte real del elemento [{i}][{j}]: "))
            imag = float(input(f"Ingrese la parte imaginaria del elemento [{i}][{j}]: "))
            fila.append(complex(real, imag))
        matriz.append(fila)
    return matriz


filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
matriz_compleja = crear_matriz_compleja(filas, columnas)

print("La matriz de números complejos creada es:")
for fila in matriz_compleja:
    print(fila)