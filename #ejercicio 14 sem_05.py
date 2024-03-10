#ejercicio 14 sem_05

def numeros_no_duplicados(nums):
    numeros_no_duplicados = set()
    numeros_duplicados = set()

    for num in nums:
        if num in numeros_no_duplicados:
            numeros_no_duplicados.remove(num)
            numeros_duplicados.add(num)
        elif num not in numeros_duplicados:
            numeros_no_duplicados.add(num)

    return numeros_no_duplicados

conjunto_numeros = {3, 1, 5, 2, 4, 2, 5}
numeros_no_duplicados_resultado = numeros_no_duplicados(conjunto_numeros)
print(numeros_no_duplicados_resultado)
