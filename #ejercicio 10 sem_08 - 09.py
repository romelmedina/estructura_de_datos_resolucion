#ejercicio 10 sem_08 - 09


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

dato_buscado = 2
if lista.buscar(dato_buscado):
    print(f"El dato {dato_buscado} está en la lista.")
else:
    print(f"El dato {dato_buscado} no está en la lista.")