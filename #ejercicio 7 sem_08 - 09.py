#ejercicio 7 sem_08 - 09


def funcion_ejemplo(x, y):
    if x > y:
        return "x es mayor que y"
    elif x < y:
        return "y es mayor que x"
    else:
        return "x es igual a y"

def asegurar_retorno_esperado():
    valor_retornado = funcion_ejemplo(5, 3)
    valor_esperado = "x es mayor que y"
    
    if valor_retornado == valor_esperado:
        print("La función retornó el valor esperado:", valor_esperado)
    else:
        print("La función no retornó el valor esperado.")

asegurar_retorno_esperado()