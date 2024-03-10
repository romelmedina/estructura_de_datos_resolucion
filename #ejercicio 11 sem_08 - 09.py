#ejercicio 11 sem_08 - 09


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

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual is not None:
            suma += actual.dato
            actual = actual.siguiente
        return suma

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

total = lista.sumar_nodos()
print( total)