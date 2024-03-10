#ejercicio 8 sem_08 - 09


def operacion_ejemplo(numero):
    resultado = numero * 2
    
    return resultado

def validar_estado_variable_despues_operacion():
    variable = 5
    
    resultado_operacion = operacion_ejemplo(variable)
    
    if resultado_operacion == variable * 2:
        print("El estado de la variable después de la operación es correcto.")
    else:
        print("El estado de la variable después de la operación es incorrecto.")

validar_estado_variable_despues_operacion()