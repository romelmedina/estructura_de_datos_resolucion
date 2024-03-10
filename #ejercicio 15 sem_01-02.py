#ejercicio 15 sem_01-02

def suma_digitos(numero):
    suma = 0
    numero_str = str(numero)
    for digito in numero_str:
        suma += int(digito)
    return suma

numero_entero = int(input("Ingrese un número entero para calcular la suma de sus dígitos: "))

resultado_suma = suma_digitos(numero_entero)

print( numero_entero,  resultado_suma)