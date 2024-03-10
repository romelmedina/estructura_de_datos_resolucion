#ejercicio 5 sem_12 - 13


def contar_nodos(arbol):
    if arbol is None:
        return 0
    
    contador = 1  
    for hijo in arbol.hijos:
        contador += contar_nodos(hijo)  
    
    return contador

raiz = Nodo('A')
raiz.agregar_hijo(Nodo('B'))
raiz.agregar_hijo(Nodo('C'))
raiz.agregar_hijo(Nodo('D'))
raiz.hijos[0].agregar_hijo(Nodo('E'))
raiz.hijos[0].agregar_hijo(Nodo('F'))
raiz.hijos[2].agregar_hijo(Nodo('G'))

cantidad_nodos = contar_nodos(raiz)
print( cantidad_nodos)
