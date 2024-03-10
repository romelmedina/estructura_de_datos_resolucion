#ejercicio 5 sem_05

def diferencia_entre_conjuntos(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

conjunto1 = {1,2,3,4,5}
conjunto2 = {4,5,6,7,8}

resultado = diferencia_entre_conjuntos(conjunto1 ,conjunto2)

print(resultado)