#ejercicio 11 sem_05

def numeros_ordenados(nums):

    nums_ordenados = sorted(nums)

    nums_ordenados = set(nums_ordenados)
    return nums_ordenados


conjunto_numeros = {3, 1, 5, 2, 4, 2, 5}
numeros_ordenados_resultado = numeros_ordenados(conjunto_numeros)
print(numeros_ordenados_resultado)