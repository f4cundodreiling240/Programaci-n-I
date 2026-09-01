def crear_estudiante(nombre:str, legajo:str, materia:str):
    return {
        "legajo": "",
        "nombre": nombre,
        "notas": [],
        "materia": ""
    }

def agregar_nota (estudiante:dict, nota:int):
    estudiante["notas"].append(nota)
    print("Nota agregada correctamente")

def ver_notas(estudiante:dict):
    if not estudiante["notas"]:
        print("No hay notas registradas")
        return

    contador = 0

    for nota in dict:
        print(f"nota {contador + 1}: {nota}")

def calcular_promedio(notas:list):
    if not notas:
        print("No hay notas registradas")
        return

    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es: {promedio}")

def buscar_nota_mayor(notas:list):
    if not notas:
        print("No hay notas registradas")
        return

    nota_mayor = 0

    for nota in notas:
        if nota > nota_mayor:
            nota_mayor = nota

    print(f"La nota mayor es: {nota_mayor}")

def calcular_media(notas:list):
    if not notas:
        print("No hay notas registradas")
        return

    media = sum(notas) / len(notas)
    print(f"La media de las notas es: {media}")

def notas_impares(notas:list):
    if not notas:
        print("No hay notas registradas")
        return

    notas_impares = []

    for nota in notas:
        if nota % 2 != 0:
            notas_impares.append(nota)

    return notas_impares

def salir(): exit()