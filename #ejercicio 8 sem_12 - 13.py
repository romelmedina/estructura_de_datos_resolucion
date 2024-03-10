#ejercicio 8 sem_12 - 13

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def altura_arbol(arbol):
    if arbol is None:
        return 0
    
    if not arbol.hijos:
        return 1
    
    alturas_hijos = [altura_arbol(hijo) for hijo in arbol.hijos]
    
    return max(alturas_hijos) + 1

raiz = Nodo('A')
raiz.agregar_hijo(Nodo('B'))
raiz.agregar_hijo(Nodo('C'))
raiz.agregar_hijo(Nodo('D'))
raiz.hijos[0].agregar_hijo(Nodo('E'))
raiz.hijos[0].agregar_hijo(Nodo('F'))
raiz.hijos[2].agregar_hijo(Nodo('G'))

altura = altura_arbol(raiz)
print( altura)
