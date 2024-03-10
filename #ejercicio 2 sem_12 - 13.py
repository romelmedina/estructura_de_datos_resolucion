#ejercicio 2 sem_12 - 13

class ColaPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def procesar_pedido(self):
        if self.pedidos:
            return self.pedidos.pop(0)
        else:
            return "No hay pedidos para procesar."

    def mostrar_estado(self):
        if self.pedidos:
            print("Estado actual de la cola de pedidos:")
            for idx, pedido in enumerate(self.pedidos, start=1):
                print(f"Pedido {idx}: {pedido}")
        else:
            print("La cola de pedidos está vacía.")

cola_pedidos = ColaPedidos()

cola_pedidos.mostrar_estado()

cola_pedidos.agregar_pedido("Pizza")
cola_pedidos.agregar_pedido("Hamburguesa")
cola_pedidos.agregar_pedido("Sushi")

cola_pedidos.mostrar_estado()

pedido_procesado = cola_pedidos.procesar_pedido()
print(pedido_procesado)

cola_pedidos.mostrar_estado()
