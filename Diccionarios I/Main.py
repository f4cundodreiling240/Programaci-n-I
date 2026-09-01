from Funciones import *

estudiantes = []

def main():
    print("Bienvenido al programa de gestión de empleados.")
    while True:
        print("\nOpciones:")
        print("1. Agregar estudiante")
        print("2. Agregar nota de estudiante")
        print("3. Promediar estudiante")
        print("4. Buscar nota mayor de estudiante")
        print("5. Calcular media de notas")
        print("6. Ver notas impares")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            legajo = input("Ingrese el legajo del estudiante: ")
            materia = input("Ingrese la materia del estudiante: ")

            nuevo_estudiante = crear_estudiante(nombre, legajo, materia)

            estudiantes.append(nuevo_estudiante)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = int(input("Ingrese la nota del estudiante: "))

            if nombre in [estudiante["nombre"] for estudiante in estudiantes]:
                estudiante = next(estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre)
                agregar_nota(estudiante, nota)
            else: print(f"No hay un estudiante {nombre}")
        elif opcion == "3":
            nombre = input("Ingrese el nombre del estudiante: ")
            
            if nombre in [estudiante["nombre"] for estudiante in estudiantes]:
                estudiante = next(estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre)
                calcular_promedio(estudiante["notas"])
            else: print(f"No hay un estudiante {nombre}")
        elif opcion == "4":
            nombre = input("Ingrese el nombre del estudiante: ")
            
            if nombre in [estudiante["nombre"] for estudiante in estudiantes]:
                estudiante = next(estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre)
                buscar_nota_mayor(estudiante["notas"])
            else: print(f"No hay un estudiante {nombre}")
        elif opcion == "5":
            nombre = input("Ingrese el nombre del estudiante: ")
            
            if nombre in [estudiante["nombre"] for estudiante in estudiantes]:
                estudiante = next(estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre)
                calcular_media(estudiante["notas"])
            else: print(f"No hay un estudiante {nombre}")
        elif opcion == "6":
            nombre = input("Ingrese el nombre del estudiante: ")
            
            if nombre in [estudiante["nombre"] for estudiante in estudiantes]:
                estudiante = next(estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre)
                notas_impares(estudiante["notas"])
            else: print(f"No hay un estudiante {nombre}")
        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()