from Funciones import *


def mostrar_menu():
    print("\n========== MENÚ ==========")
    print("1. Agregar temperaturas")
    print("2. Ver temperaturas")
    print("3. Calcular promedio")
    print("4. Buscar mayor")
    print("5. Buscar menor")
    print("6. Contar temperatura")
    print("7. Ordenar temperaturas (Método Burbuja)")
    print("8. Salir")
    print("==========================")


def main():
    temperaturas = []

    # Cargar las temperaturas guardadas en el archivo
    cargar_archivo(temperaturas)

    opcion = 0

    while opcion != 8:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                agregar_temperatura(temperaturas)
                guardar_archivo(temperaturas)

            elif opcion == 2:
                ver_temperaturas(temperaturas)

            elif opcion == 3:
                calcular_promedio(temperaturas)

            elif opcion == 4:
                buscar_mayor(temperaturas)

            elif opcion == 5:
                buscar_menor(temperaturas)

            elif opcion == 6:
                contar_temperatura(temperaturas)

            elif opcion == 7:
                ordenar_temperaturas(temperaturas)
                guardar_archivo(temperaturas)

            elif opcion == 8:
                guardar_archivo(temperaturas)
                print("Programa finalizado.")

            else:
                print("Opción inválida. Intente nuevamente.")

        except ValueError:
            print("Debe ingresar un número válido.")


main()