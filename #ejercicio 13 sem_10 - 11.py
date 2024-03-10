#ejercicio 13 sem_10 - 11

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def es_palindromo(palabra):
    palabra = palabra.lower() 
    caracteres_validos = 'abcdefghijklmnopqrstuvwxyz'

    palabra_filtrada = ''.join(caracter for caracter in palabra if caracter in caracteres_validos)

    longitud = len(palabra_filtrada)
    mitad = longitud // 2
    pila = Pila()

    for caracter in palabra_filtrada[:mitad]:
        pila.apilar(caracter)

    for caracter in palabra_filtrada[mitad + longitud % 2:]:
        if caracter != pila.desapilar():
            return False

    return True

palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')
