#ejercicio 20 sem_05

def palabras_palindromas_y_longitud(palabras, longitud):
    palabras_palindromas = set()
    for palabra in palabras:
        if len(palabra) == longitud and palabra == palabra[::-1]:
            palabras_palindromas.add(palabra)
    palabras_palindromas_ordenadas = sorted(palabras_palindromas)
    return palabras_palindromas_ordenadas


conjunto_palabras = {"hola", "ala", "adiós", "casa", "radar", "sol", "reconocer"}
longitud_deseada = 3
palabras_palindromas_resultado = palabras_palindromas_y_longitud(conjunto_palabras, longitud_deseada)
print(palabras_palindromas_resultado)