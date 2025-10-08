from collections import deque

def cola_impresion():
    cola = deque()
    cola.append("documento.pdf")
    cola.append("facturaTIGO.pdf")
    cola.append("libro1.xlsx")
    cola.append("doc1.docx")

    print("Cola de impresión inicializada: ",list(cola))

    impreso = cola.popleft()
    print(f"Imprimiendo {impreso}...")
    print(f"Cola restante: ",list(cola))

cola_impresion()