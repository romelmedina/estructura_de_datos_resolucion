#ejercicio 9 sem_01-02

def contar_vocales(cadena):

    cadena = cadena.lower()
    contador = 0

    vocales = "aeiou"
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador


texto = input("Ingrese una cadena de texto para contar las vocales: ")


num_vocales = contar_vocales(texto)

print(num_vocales)