def simulador_deshacer():
    pila_acciones = []
    while True:
        print("Simulador de deshacer")
        print("1. Realizar acción")
        print("2. Deshacer última acción")
        print("3. Mostrar historial")
        print("4. Salir")

        option = input("Ingresa una opción(1-4): ")

        match option:
            case "1":
                accion = input("Ingresa la acción: ")
                pila_acciones.append(accion)
                print(f"La acción '{accion}' guardada.")

            case "2":
                if pila_acciones:
                    ultima = pila_acciones.pop()
                    print(f"Acción '{ultima}' deshecha.")
                else:
                    print("No hay acciones para deshacer.")

            case "3":
                print("Historial de acciones: ",pila_acciones)

            case "4":
                print("Programa finalizado y saliendo...")
                break

            case _:
                print("Opción no válida. Inténtalo nuevamente.")

simulador_deshacer()