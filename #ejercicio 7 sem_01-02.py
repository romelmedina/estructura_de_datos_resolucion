#ejercicio 7 sem_01-02

def suma_numeros_pares(rango_inicio, rango_fin):
    suma = 0

    for numero in range(rango_inicio, rango_fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma


inicio = int(input("Ingrese el número inicial del rango: "))
fin = int(input("Ingrese el número final del rango: "))

resultado_suma = suma_numeros_pares(inicio, fin)


print( inicio, "a", fin, "es:", resultado_suma)