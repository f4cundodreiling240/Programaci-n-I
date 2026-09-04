from Funciones import *

def opciones_principales():
    while True:
        try:
            e = int(input(
                "1: Ver platos disponibles\n"
                "2: Ver plato específico\n"
                "3: Hacer pedido\n"
                "0: Salir\n"
            ))

            if e == 1:
                mostrar_platos()

                sig = input("Presione enter para continuar...")

            elif e == 2:
                nombre_plato = input("Ingrese el nombre del plato que desea ver: ")

                mostrar_plato(nombre_plato)

            elif e == 3:
                pedido_datos = {
                    "nombre_cliente": "",
                    "apellido_cliente": "",
                    "prioridad": "",
                    "plato_ordenado": ""
                }

                nombre_cliente = input("Ingrese su nombre: ")
                apellido_cliente = input("Ingrese su apellido: ")

                prioridad = input("Ingrese la prioridad del pedido (baja, normal, alta): ")

                prioridades = ("baja", "normal", "alta")

                if not prioridad.lower().replace(" ", "").strip() in prioridades:
                    prioridad = "baja"

                plato_nombre = input("Ingrese el nombre del plato que desea ordenar: ")

                plato_ordenado = obtener_plato(plato_nombre)

                pedido_datos["nombre_cliente"] = nombre_cliente
                pedido_datos["apellido_cliente"] = apellido_cliente
                pedido_datos["prioridad"] = prioridad
                pedido_datos["plato_ordenado"] = plato_ordenado

                if not plato_ordenado == None:
                    ordenar_pedido(pedido_datos) 

                else: print("El plato que ingresó no existe.")

            elif e == 0: 
                print("Saliendo del programa, ¡Hasta luego!")
                break

            else: print("Ingrese una opción válida.")
                    
        except ValueError:
            print("Ingrese solo números.")

opciones_principales()