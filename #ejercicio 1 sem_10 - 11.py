#ejercicio 1 sem_10 - 11

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

    def duplicar_nodos(self):
        actual = self.cabeza
        while actual is not None:
            nodo_duplicado = Nodo(actual.dato)
            nodo_duplicado.siguiente = actual.siguiente
            actual.siguiente = nodo_duplicado
            actual = nodo_duplicado.siguiente

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

# Crear la lista original
lista_original = ListaEnlazada()
lista_original.agregar(1)
lista_original.agregar(2)
lista_original.agregar(3)
lista_original.agregar(4)

lista_original.duplicar_nodos()

lista_original.imprimir_adelante()
lista_original.imprimir_atras()

lista_original.cabeza = lista_original.cabeza.siguiente 
lista_original.imprimir_adelante()
lista_original.imprimir_atras()
