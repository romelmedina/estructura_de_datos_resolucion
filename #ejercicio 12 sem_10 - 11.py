#ejercicio 12 sem_10 - 11

def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def evaluar_expresion(expresion):
    pila = Pila()
    operadores = "+-*/"

    for caracter in expresion:
        if caracter.isdigit():  
            pila.apilar(int(caracter))
        elif caracter in operadores:  
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if caracter == '+':
                resultado = operando1 + operando2
            elif caracter == '-':
                resultado = operando1 - operando2
            elif caracter == '*':
                resultado = operando1 * operando2
            elif caracter == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)

    return pila.desapilar()  

expresion = "3+4*2-5/1"
resultado = evaluar_expresion(expresion)
print( resultado)
