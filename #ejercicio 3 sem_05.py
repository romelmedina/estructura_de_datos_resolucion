#ejercicio 3 sem_05

def nuemros_divisibles (conjunto , divisor) :
    divisibles = set()
    for numero in conjunto:
        if numero % divisor == 0:
            divisible.add(numero)

    return divisibles

conjunto = {1,2,3,4,5,6,7,8,9,10}

divisor = 2
resultado = nuemros_divisibles(conjunto , divisor)

print(resultado)