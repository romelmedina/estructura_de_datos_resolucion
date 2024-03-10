#ejercicio 9 sem_08 - 09


def asegurar_importacion_modulo():
    try:
        import modulo_inexistente  # Intenta importar el módulo
        print("El módulo se ha importado correctamente.")
    except ImportError:
        print("No se pudo importar el módulo.")

asegurar_importacion_modulo()