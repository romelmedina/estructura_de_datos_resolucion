#ejercicio 4 sem_01-02

def factorial(numero):

    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i
    return resultado


numero = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero)
print( numero,  resultado_factorial)