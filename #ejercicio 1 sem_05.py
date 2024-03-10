#ejercicio 1 sem_05

conjunto = {1,2,3,4,5,6,7,8,9,10}


def es_primo (numero):
    if numero <= 1 :
        return False
    for i in range(2 , int(numero **0.5) + 1):
        if numero % i == 0 :
            return False
        return True
    
def numeros_primos (conjunto):
    primos = set()
    for num in conjunto:
        if es_primo(num):
            primos.add(num)
    return primos

resultado = numeros_primos(conjunto)

print(resultado)