#ejercicio 4 sem_05

def numeros_comunes (conjunto1 , conjunto2):
    return conjunto1.intersection(conjunto2)

conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}

resultado = numeros_comunes(conjunto1,conjunto2)
print(resultado)