#ejercicio 11 sem_10 - 11

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

def eliminar_duplicados_pila(pila):
    pila_auxiliar = Pila()
    elementos_vistos = set()

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_vistos:
            pila_auxiliar.apilar(elemento)
            elementos_vistos.add(elemento)
    while not pila_auxiliar.esta_vacia():
        pila.apilar(pila_auxiliar.desapilar())

mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(2)
mi_pila.apilar(9)
mi_pila.apilar(3)
mi_pila.apilar(5)
mi_pila.apilar(7)
mi_pila.apilar(2)

print(mi_pila.items)

eliminar_duplicados_pila(mi_pila)

print( mi_pila.items)