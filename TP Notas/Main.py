from Funciones import *

def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE NOTAS ===")
    print("1. Agregar nota")
    print("2. Ver notas")
    print("3. Calcular promedio")
    print("4. Buscar nota mayor")
    print("5. Calcular Media")
    print("6. Ver solamente notas impares")
    print("7. Salir")


notas = []
opcion = 0

while opcion != 7:
    mostrar_menu()

    try:
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            try:
                nota = float(input("Ingrese la nota: "))

                if nota < 0 or nota > 10:
                    print("La nota debe estar entre 0 y 10.")
                else:
                    # Se utiliza append() directamente, como solicita
                    # el enunciado.
                    notas.append(nota)
                    print("Nota agregada correctamente.")

            except ValueError:
                print("Debe ingresar un número válido.")

        elif opcion == 2:
            ver_notas(notas)

        elif opcion == 3:
            if len(notas) == 0:
                print("No hay notas para calcular el promedio.")
            else:
                promedio = calcular_promedio(notas)
                print("Promedio:", promedio)

        elif opcion == 4:
            mayor = buscar_nota_mayor(notas)

            if mayor is None:
                print("No hay notas cargadas.")
            else:
                print("La nota mayor es:", mayor)

        elif opcion == 5:
            media = calcular_media(notas)

            if media is None:
                print("No hay notas para calcular la media.")
            else:
                print("La media es:", media)

        elif opcion == 6:
            notas_impares = obtener_notas_impares(notas)

            if len(notas_impares) == 0:
                print("No hay notas impares.")
            else:
                # Reutilizamos la función ver_notas() para mostrar
                # las notas impares.
                ver_notas(notas_impares)

        elif opcion == 7:
            print("Programa finalizado.")

        else:
            print("Opción inválida. Seleccione una opción del 1 al 7.")

    except ValueError:
        print("Debe ingresar un número entero.")
