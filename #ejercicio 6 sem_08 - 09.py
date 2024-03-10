#ejercicio 6 sem_08 - 09


def ejecutar_ciclo_al_menos_una_vez():
    continuar = True
    
    while continuar:
        nombre = input("Ingrese su nombre: ")
        print("¡Hola,", nombre, "!")

        respuesta = input("¿Desea continuar? (s/n): ")
        
        if respuesta.lower() != 's':
            continuar = False

ejecutar_ciclo_al_menos_una_vez()