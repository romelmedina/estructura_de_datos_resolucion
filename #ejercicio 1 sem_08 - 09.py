#ejercicio 1 sem_08 - 09

def validar_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                print("La edad no puede ser un número negativo. Por favor, ingrese un valor válido.")
            elif edad < 18:
                print("Debe ser mayor de edad para utilizar este servicio.")
            else:
                print("Edad válida")
                break
        except ValueError:
            print("ingrese un número entero para la edad.")

validar_edad()
