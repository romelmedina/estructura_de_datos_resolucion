#ejercicio 12 sem_01-02

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

palabra = input("Ingrese una palabra para verificar si es un palíndromo: ")

if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")