#ejercicio 4 sem_10 - 11


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
datos_duplicados = [1, 2, 2, 3, 4, 4, 5]
for dato in datos_duplicados:
    lista.agregar(dato)

lista.eliminar_duplicados()
lista.imprimir_adelante()
lista.imprimir_atras()