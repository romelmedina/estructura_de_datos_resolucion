#ejercicio 11 sem_01-02

numeros = input("Ingrese una lista de números separados por espacios: ")

lista_numeros = [float(numero) for numero in numeros.split()]

lista_numeros_ordenada = sorted(lista_numeros)

print("Lista de números ordenada de menor a mayor:", lista_numeros_ordenada)