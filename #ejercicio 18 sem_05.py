#ejercicio 18 sem_05

def palabras_con_letra_y_ordenadas(palabras, letra):
    palabras_con_letra = set()
    for palabra in palabras:
        if letra in palabra:
            palabras_con_letra.add(palabra)
    palabras_con_letra_ordenadas = sorted(palabras_con_letra, reverse=True)
    return palabras_con_letra_ordenadas


conjunto_palabras = {"hola", "adiós", "casa", "perro", "gato", "amor", "sol"}
letra_deseada = "o"
palabras_con_letra_resultado = palabras_con_letra_y_ordenadas(conjunto_palabras, letra_deseada)

print(palabras_con_letra_resultado)