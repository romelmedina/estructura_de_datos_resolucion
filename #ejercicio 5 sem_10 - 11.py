#ejercicio 5 sem_10 - 11


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

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        nodos = []
        actual = self.cabeza
        while actual is not None:
            nodos.append(actual.dato)
            actual = actual.siguiente
        for dato in reversed(nodos):
            print(dato, end=" ")
        print()

lista = ListaEnlazada()
for dato in range(1, 7):
    lista.agregar(dato)

lista.invertir()
lista.imprimir_adelante()
lista.imprimir_atras()