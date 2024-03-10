#ejercicio 10 sem_01-02

def fibonacci(n):
    fibonacci_lista = [0, 1]
    for i in range(2, n):

        siguiente_fibonacci = fibonacci_lista[-1] + fibonacci_lista[-2]
        fibonacci_lista.append(siguiente_fibonacci)
    return fibonacci_lista


primeros_10_fibonacci = fibonacci(10)

print(primeros_10_fibonacci)