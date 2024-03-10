#ejercicio 2 sem_10 - 11


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

    def contar_par_impar(self):
        contador_par = 0
        contador_impar = 0
        actual = self.cabeza
        while actual is not None:
            if actual.dato % 2 == 0:
                contador_par += 1
            else:
                contador_impar += 1
            actual = actual.siguiente
        return contador_par, contador_impar

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
for dato in range(1, 10):
    lista.agregar(dato)

par, impar = lista.contar_par_impar()
print( par)
print( impar)

lista.imprimir_adelante()
lista.imprimir_atras()