from collections import deque

def cola_pedidos():
    cola = deque()
    cola.append("Capuccino")
    cola.append("Mocaccino")
    cola.append("Café con leche")
    cola.append("Café Guatemalteco")

    print(f"Cola de pedidos inicializada:", list(cola))

    finalizado = cola.popleft()
    print(f"Pedido procesado de {finalizado}")
    print("Pedidos restantes: ",list(cola))

cola_pedidos()