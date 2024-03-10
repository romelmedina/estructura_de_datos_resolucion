#ejercicio 13 sem_08 - 09

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

    def concatenar(self, otra_lista):
        if self.cabeza is None:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

lista1 = ListaEnlazada()
lista1.agregar(1)
lista1.agregar(2)
lista1.agregar(3)

lista2 = ListaEnlazada()
lista2.agregar(4)
lista2.agregar(5)
lista2.agregar(6)

print("Lista 1:")
lista1.imprimir()
print("Lista 2:")
lista2.imprimir()
lista1.concatenar(lista2)
lista1.imprimir()