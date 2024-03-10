#ejercicio 9 sem_12 - 13

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def profundidad_nodo(arbol, valor_nodo, profundidad_actual=0):
    if arbol is None:
        return 0
    
    if arbol.valor == valor_nodo:
        return profundidad_actual
    
    for hijo in arbol.hijos:
        profundidad = profundidad_nodo(hijo, valor_nodo, profundidad_actual + 1)
        if profundidad:  
            return profundidad
    
    return 0

raiz = Nodo('A')
raiz.agregar_hijo(Nodo('B'))
raiz.agregar_hijo(Nodo('C'))
raiz.agregar_hijo(Nodo('D'))
raiz.hijos[0].agregar_hijo(Nodo('E'))
raiz.hijos[0].agregar_hijo(Nodo('F'))
raiz.hijos[2].agregar_hijo(Nodo('G'))

nodo_buscar = 'F'
profundidad = profundidad_nodo(raiz, nodo_buscar)
if profundidad:
    print(f"La profundidad del nodo '{nodo_buscar}' es:", profundidad)
else:
    print(f"No se encontró el nodo '{nodo_buscar}'.")
