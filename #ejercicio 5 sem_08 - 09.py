#ejercicio 5 sem_08 - 09

def validar_igualdad(objeto1, objeto2):
    if objeto1 == objeto2:
        print("Los objetos son iguales.")
    else:
        print("Los objetos son diferentes.")

objeto1 = [1, 2, 3]
objeto2 = [1, 2, 3]
objeto3 = objeto1  

validar_igualdad(objeto1, objeto2)
validar_igualdad(objeto1, objeto3)