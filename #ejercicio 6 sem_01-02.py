#ejercicio 6 sem_01-02

def invertir_cadena(cadena):

    cadena_invertida = cadena[::-1]
    return cadena_invertida


texto = input("Ingrese una cadena de texto para invertirla: ")


texto_invertido = invertir_cadena(texto)

print("La cadena invertida es:", texto_invertido)