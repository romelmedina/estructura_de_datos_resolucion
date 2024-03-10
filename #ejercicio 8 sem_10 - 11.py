#ejercicio 8 sem_10 - 11

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

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for token in expresion.split():
        if token.isdigit():  
            pila.apilar(int(token))
        else:  
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            resultado = operadores[token](operando1, operando2)
            pila.apilar(resultado)

    return pila.desapilar() 

expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print( resultado)