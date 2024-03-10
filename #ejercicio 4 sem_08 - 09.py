#ejercicio 4 sem_08 - 09


def asegurar_lista_no_vacia(lista):
    if len(lista) > 0:
        print("La lista no está vacía.")
    else:
        print("La lista está vacía.")

lista1 = [1, 2, 3]
lista2 = []

asegurar_lista_no_vacia(lista1)
asegurar_lista_no_vacia(lista2)