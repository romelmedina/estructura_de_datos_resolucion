#ejercicio 8 sem_05

def es_palindromo (palabra):
    return palabra == palabra[::-1]

def palindromos_conjunto(conjunto):
    palindromos =set ()
    for palabra in conjunto:
        if es_palindromo(palabra):
            palindromos.add(palabra)
    
    return palindromos

conjunto_palabras = {"radar", " oso", "casa", "ana", "nivel"}

resultado = palindromos_conjunto(conjunto_palabras)
print(resultado)