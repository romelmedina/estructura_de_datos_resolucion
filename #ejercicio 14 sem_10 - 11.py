#ejercicio 14 sem_10 - 11

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def deshacer(acciones, deshaceres):
    if not acciones.esta_vacia():
        accion = acciones.desapilar()
        deshaceres.apilar(accion)
        print("Deshacer:", accion)
    else:
        print("No hay acciones para deshacer.")

def rehacer(acciones, deshaceres):
    if not deshaceres.esta_vacia():
        accion = deshaceres.desapilar()
        acciones.apilar(accion)
        print("Rehacer:", accion)
    else:
        print("No hay acciones para rehacer.")

acciones_realizadas = Pila()
acciones_deshacer = Pila()

acciones_realizadas.apilar("Accion 1")
acciones_realizadas.apilar("Accion 2")
acciones_realizadas.apilar("Accion 3")

deshacer(acciones_realizadas, acciones_deshacer)  
deshacer(acciones_realizadas, acciones_deshacer)  

rehacer(acciones_realizadas, acciones_deshacer)
