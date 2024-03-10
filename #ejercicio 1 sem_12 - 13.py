#ejercicio 1 sem_12 - 13


class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

def es_palindroma(palabra):
    cola = Cola()

    for caracter in palabra:
        cola.encolar(caracter)

    palabra_inversa = palabra[::-1]

    while not cola.esta_vacia():
        if cola.desencolar() != palabra_inversa[0]:
            return False
        palabra_inversa = palabra_inversa[1:]

    return True

palabra = "reconocer"
if es_palindroma(palabra):
    print(f'La palabra "{palabra}" es palíndroma.')
else:
    print(f'La palabra "{palabra}" no es palíndroma.')
