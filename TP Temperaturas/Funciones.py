def agregar_temperatura(temperaturas):
    temperatura = float(input("Ingrese la temperatura: "))
    temperaturas.append(temperatura)
    print("Temperatura agregada correctamente.")


def ver_temperaturas(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        print("\nTemperaturas:")
        for i, temperatura in enumerate(temperaturas, 1):
            print(f"{i}. {temperatura} °C")


def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas para calcular el promedio.")
    else:
        promedio = sum(temperaturas) / len(temperaturas)
        print(f"El promedio es: {promedio:.2f} °C")


def buscar_mayor(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        print(f"La temperatura mayor es: {max(temperaturas)} °C")


def buscar_menor(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        print(f"La temperatura menor es: {min(temperaturas)} °C")


def contar_temperatura(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        temperatura = float(input("Ingrese la temperatura a buscar: "))
        cantidad = temperaturas.count(temperatura)
        print(f"La temperatura {temperatura} °C se repite {cantidad} vez/veces.")


def ordenar_temperaturas(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas para ordenar.")
    else:
        # Método de Burbuja
        for i in range(len(temperaturas) - 1):
            for j in range(len(temperaturas) - 1 - i):
                if temperaturas[j] > temperaturas[j + 1]:
                    temperaturas[j], temperaturas[j + 1] = \
                        temperaturas[j + 1], temperaturas[j]

        print("Temperaturas ordenadas correctamente.")
        ver_temperaturas(temperaturas)


def cargar_archivo(temperaturas):
    try:
        archivo = open("temperaturas.txt", "r")

        for linea in archivo:
            temperaturas.append(float(linea.strip()))

        archivo.close()

    except FileNotFoundError:
        
        pass


def guardar_archivo(temperaturas):
    archivo = open("temperaturas.txt", "w")

    for temperatura in temperaturas:
        archivo.write(str(temperatura) + "\n")

    archivo.close()
