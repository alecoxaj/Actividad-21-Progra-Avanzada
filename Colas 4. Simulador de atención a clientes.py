from collections import deque

def simulador_clientes():
    cola = deque()
    cola.append("Giselle")
    cola.append("Alejandro")
    cola.append("Elly")
    cola.append("Francisco")

    print(f"Cola Inicial: ", list(cola))

    atendido = cola.popleft()
    print(f"Cliente atendido: {atendido}")
    print("Cola actual: ", list(cola))

simulador_clientes()