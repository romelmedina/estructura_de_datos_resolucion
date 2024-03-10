#ejercicio 13 sem_05


def numeros_duplicados(nums):
    numeros_duplicados = set()
    numeros_repetidos = set()

    for num in nums:
        if num in numeros_duplicados:
            numeros_repetidos.add(num)
        else:
            numeros_duplicados.add(num)

    return numeros_repetidos


conjunto_numeros = {3, 1, 5, 2, 4, 2, 5}
numeros_duplicados_resultado = numeros_duplicados(conjunto_numeros)
print(numeros_duplicados_resultado)