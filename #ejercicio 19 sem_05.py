#ejercicio 19 sem_05

def numeros_ordenados_no_duplicados(nums):
    nums_ordenados = sorted(nums)
    nums_no_duplicados = []
    for num in nums_ordenados:
        if num not in nums_no_duplicados:
            nums_no_duplicados.append(num)
    return set(nums_no_duplicados)


conjunto_numeros = {3, 1, 5, 2, 4, 2, 5}
numeros_ordenados_no_duplicados_resultado = numeros_ordenados_no_duplicados(conjunto_numeros)
print(numeros_ordenados_no_duplicados_resultado)