#ejercicio 10 sem_12 - 13

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def encontrar_valor_minimo(arbol):
    if arbol is None:
        return None
    
    valor_minimo = arbol.valor
    
    for hijo in arbol.hijos:
        valor_minimo_hijo = encontrar_valor_minimo(hijo)
        if valor_minimo_hijo is not None and valor_minimo_hijo < valor_minimo:
            valor_minimo = valor_minimo_hijo
    
    return valor_minimo

raiz = Nodo(5)
raiz.agregar_hijo(Nodo(3))
raiz.agregar_hijo(Nodo(8))
raiz.agregar_hijo(Nodo(1))
raiz.hijos[0].agregar_hijo(Nodo(4))
raiz.hijos[0].agregar_hijo(Nodo(2))
raiz.hijos[2].agregar_hijo(Nodo(7))

valor_minimo = encontrar_valor_minimo(raiz)
print( valor_minimo)
