#ejercicio 13 sem_01-02

numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))

print(f"Tabla de multiplicar del número {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")