#ejercicio 3 sem_08 - 09

def validar_calificacion():
    while True:
        try:
            calificacion = float(input("Ingrese su calificación: "))
            if calificacion < 0 or calificacion > 10:
                print("La calificación debe estar en el rango de 0 a 10. Por favor, ingrese un valor válido.")
            else:
                print("¡Calificación válida!")
                break
        except ValueError:
            print("Por favor, ingrese un número para la calificación.")

validar_calificacion()