#ejercicio 15 sem_08 - 09


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

    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual is not None:
            siguiente_temporal = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente_temporal
        self.cabeza = previo

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

lista.imprimir()
lista.invertir()
lista.imprimir()