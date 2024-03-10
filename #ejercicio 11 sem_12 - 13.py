#ejercicio 11 sem_12 - 13

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def encontrar_valor_maximo(arbol):
    if arbol is None:
        return None
    
    valor_maximo = arbol.valor
    
    for hijo in arbol.hijos:
        valor_maximo_hijo = encontrar_valor_maximo(hijo)
        if valor_maximo_hijo is not None and valor_maximo_hijo > valor_maximo:
            valor_maximo = valor_maximo_hijo
    
    return valor_maximo

raiz = Nodo(5)
raiz.agregar_hijo(Nodo(3))
raiz.agregar_hijo(Nodo(8))
raiz.agregar_hijo(Nodo(1))
raiz.hijos[0].agregar_hijo(Nodo(4))
raiz.hijos[0].agregar_hijo(Nodo(2))
raiz.hijos[2].agregar_hijo(Nodo(7))

valor_maximo = encontrar_valor_maximo(raiz)
print( valor_maximo)

