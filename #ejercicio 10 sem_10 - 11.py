#ejercicio 10 sem_10 - 11

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

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

def ordenar_pila_ascendente(pila):
    pila_auxiliar = Pila()

    while not pila.esta_vacia():
        temp = pila.desapilar()

        while not pila_auxiliar.esta_vacia() and pila_auxiliar.ver_tope() > temp:
            pila.apilar(pila_auxiliar.desapilar())

        pila_auxiliar.apilar(temp)

    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(2)
mi_pila.apilar(9)
mi_pila.apilar(3)
mi_pila.apilar(7)

print(mi_pila.items)
ordenar_pila_ascendente(mi_pila)
print( mi_pila.items)