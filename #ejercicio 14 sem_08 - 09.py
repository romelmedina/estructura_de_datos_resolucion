#ejercicio 14 sem_08 - 09

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

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        valores_vistos = set([self.cabeza.dato])
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.dato in valores_vistos:
                actual.siguiente = actual.siguiente.siguiente
            else:
                valores_vistos.add(actual.siguiente.dato)
                actual = actual.siguiente

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(1)
lista.agregar(3)
lista.agregar(2)
lista.agregar(4)


lista.imprimir()
lista.eliminar_duplicados()
lista.imprimir()