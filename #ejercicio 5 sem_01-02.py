#ejercicio 5 sem_01-02

def es_primo(numero):

    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


numero = int(input("Ingrese un número para verificar si es primo: "))

if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")