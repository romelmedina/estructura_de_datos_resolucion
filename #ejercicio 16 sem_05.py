#ejercicio 16 sem_05

def es_palindromo(palabra):

    return palabra == palabra[::-1]

def palabras_palindromas_ordenadas(palabras):
    palabras_palindromas = set()
    for palabra in palabras:
        if es_palindromo(palabra):
            palabras_palindromas.add(palabra)
    palabras_palindromas_ordenadas = sorted(palabras_palindromas)
    return palabras_palindromas_ordenadas

conjunto_palabras = {"ana", "oso", "casa", "radar", "sol", "reconocer"}
palabras_palindromas_resultado = palabras_palindromas_ordenadas(conjunto_palabras)
print(palabras_palindromas_resultado)