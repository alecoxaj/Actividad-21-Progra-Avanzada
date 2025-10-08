def decimal_a_binario(numero):
    pila = []

    if numero == 0:
        return "0"

    while numero > 0:
        resto = numero % 2
        pila.append(str(resto))
        numero //= 2

    binario = ""
    while pila:
        binario += pila.pop()

    return binario


num = int(input("Ingresa un número decimal: "))
print(f"El número binario es: {decimal_a_binario(num)}")

