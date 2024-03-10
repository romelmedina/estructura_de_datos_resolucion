#ejercicio 3 sem_10 - 11


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

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if posicion == 1:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for _ in range(1, posicion - 1):
                if actual is None:
                    print("Posición inválida.")
                    return
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

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
for dato in range(1, 6):
    lista.agregar(dato)

lista.insertar_en_posicion(15, 3)
lista.imprimir_adelante()
lista.imprimir_atras()