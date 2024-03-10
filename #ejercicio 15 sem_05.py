#ejercicio 15 sem_05

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos_ordenados(nums):
    numeros_primos = set()
    for num in nums:
        if es_primo(num):
            numeros_primos.add(num)
    numeros_primos_ordenados = sorted(numeros_primos)
    return numeros_primos_ordenados

conjunto_numeros = {3, 1, 5, 2, 4, 7, 8, 11}
numeros_primos_resultado = numeros_primos_ordenados(conjunto_numeros)
print(numeros_primos_resultado)