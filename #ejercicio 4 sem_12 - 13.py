#ejercicio 4 sem_12 - 13

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        self.tareas.append({"descripcion": descripcion, "completada": False})

    def marcar_completada(self, indice_tarea):
        if 0 <= indice_tarea < len(self.tareas):
            self.tareas[indice_tarea]["completada"] = True
        else:
            print("El índice de la tarea no es válido.")

    def mostrar_proxima_pendiente(self):
        for tarea in self.tareas:
            if not tarea["completada"]:
                print( tarea["descripcion"])
                return
        print("No hay tareas pendientes.")

sistema_tareas = SistemaGestionTareas()

sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Enviar correo electrónico")
sistema_tareas.agregar_tarea("Preparar informe")

sistema_tareas.mostrar_proxima_pendiente()

sistema_tareas.marcar_completada(0)

sistema_tareas.mostrar_proxima_pendiente()
