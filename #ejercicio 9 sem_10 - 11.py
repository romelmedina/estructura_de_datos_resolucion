#ejercicio 9 sem_10 - 11


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

def operadores_anidados_correctamente(expresion):
    pila = Pila()
    operadores_abiertos = "([{"
    operadores_cerrados = ")]}"

    for caracter in expresion:
        if caracter in operadores_abiertos:
            pila.apilar(caracter)
        elif caracter in operadores_cerrados:
            if pila.esta_vacia() or operadores_abiertos.index(pila.desapilar()) != operadores_cerrados.index(caracter):
                return False

    return pila.esta_vacia()

expresion = "(3 + 2) * (4 - 1)"
if operadores_anidados_correctamente(expresion):
    print( expresion)
else:
    print( expresion)