#ejercicio 17 sem_05

def palabras_con_longitud(palabras, longitud):
    palabras_con_longitud = set()
    for palabra in palabras:
        if len(palabra) == longitud:
            palabras_con_longitud.add(palabra)
    palabras_con_longitud_ordenadas = sorted(palabras_con_longitud)
    return palabras_con_longitud_ordenadas


conjunto_palabras = {"hola", "adiós", "casa", "perro", "gato", "amor", "sol"}
longitud_deseada = 4
palabras_con_longitud_resultado = palabras_con_longitud(conjunto_palabras, longitud_deseada)
print(palabras_con_longitud_resultado)