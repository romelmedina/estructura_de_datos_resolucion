#ejercicio 7 sem_12 - 13


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def contar_nodos_internos(arbol):
    if arbol is None:
        return 0
    
    if arbol.hijos: 
        contador = 1
    else:
        contador = 0
    
    for hijo in arbol.hijos:
        contador += contar_nodos_internos(hijo) 
    
    return contador

raiz = Nodo('A')
raiz.agregar_hijo(Nodo('B'))
raiz.agregar_hijo(Nodo('C'))
raiz.agregar_hijo(Nodo('D'))
raiz.hijos[0].agregar_hijo(Nodo('E'))
raiz.hijos[0].agregar_hijo(Nodo('F'))
raiz.hijos[2].agregar_hijo(Nodo('G'))

cantidad_nodos_internos = contar_nodos_internos(raiz)
print(cantidad_nodos_internos)
