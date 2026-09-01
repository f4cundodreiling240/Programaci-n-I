def ver_notas(notas):
    """Muestra todas las notas de la lista."""
    if len(notas) == 0:
        print("No hay notas cargadas.")
    else:
        print("\n--- NOTAS ---")
        posicion = 0

        while posicion < len(notas):
            print("Nota", posicion + 1, ":", notas[posicion])
            posicion += 1


def calcular_promedio(notas):
    """Calcula y devuelve el promedio de las notas manualmente."""
    if len(notas) == 0:
        return 0

    total = 0
    cantidad = 0

    for nota in notas:
        total += nota
        cantidad += 1

    promedio = total / cantidad
    return promedio


def buscar_nota_mayor(notas):
    """Busca y devuelve la nota mayor manualmente."""
    if len(notas) == 0:
        return None

    mayor = notas[0]

    for nota in notas:
        if nota > mayor:
            mayor = nota

    return mayor


def calcular_media(notas):
    """Calcula la mediana de las notas manualmente."""
    if len(notas) == 0:
        return None

    # Crear una copia sin utilizar .copy(), .sort() ni métodos
    # de ordenamiento.
    ordenadas = []

    for nota in notas:
        ordenadas.append(nota)

    # Ordenamiento burbuja manual
    i = 0

    while i < len(ordenadas) - 1:
        j = 0

        while j < len(ordenadas) - 1 - i:
            if ordenadas[j] > ordenadas[j + 1]:
                auxiliar = ordenadas[j]
                ordenadas[j] = ordenadas[j + 1]
                ordenadas[j + 1] = auxiliar

            j += 1

        i += 1

    cantidad = len(ordenadas)

    if cantidad % 2 != 0:
        # Cantidad impar: la media es el elemento central
        posicion_central = cantidad // 2
        media = ordenadas[posicion_central]
    else:
        # Cantidad par: promedio de los dos elementos centrales
        posicion1 = cantidad // 2 - 1
        posicion2 = cantidad // 2

        media = (ordenadas[posicion1] + ordenadas[posicion2]) / 2

    return media


def obtener_notas_impares(notas):
    """Devuelve una lista con solamente las notas impares."""
    impares = []

    for nota in notas:
        if nota % 2 != 0:
            impares.append(nota)

    return impares
