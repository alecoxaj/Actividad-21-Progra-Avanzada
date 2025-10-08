def verificar_parentesis(expresion):
    pila = []
    for caracter in expresion:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila:
                return f"Paréntesis no balanceados"
            pila.pop()
    if not pila:
        return f"Paréntesis balanceados"
    else:
        return f"Paréntesis no balanceados"


exp = input("Ingresa una expresión matemática: ")
print(verificar_parentesis(exp))