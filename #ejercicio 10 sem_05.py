#ejercicio 10 sem_05

def palabras_con_letra(palabras, letra):
    palabras_con_letra = set()
    for palabra in palabras:
        if letra in palabra:
            palabras_con_letra.add(palabra)
    return palabras_con_letra

conjunto_palabras = {"hola", "adiós", "casa", "perro", "gato"}
letra_busqueda = "o"
palabras_encontradas = palabras_con_letra(conjunto_palabras, letra_busqueda)
print(palabras_encontradas)