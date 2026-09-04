class Plato():
    def __init__ (self, nombre:str, precio:int, ingredientes:list):
        self.nombre = nombre
        self.precio = precio

        self.ingredientes = ingredientes

platos = []

def crear_plato(nombre:str, precio:int, ingredientes:list):
    nuevo_plato = Plato(nombre, precio, ingredientes)

    platos.append(nuevo_plato)

crear_plato("Fideos con queso", 7000, ["Fideos", "Queso rallado"])
crear_plato("Fideos con tuco", 7500, ["Fideos", "Salsa de tuco", "Albóndigas"])
crear_plato("Fideos con salsa_blanca", 7000, ["Fideos", "Salsa blanca"])

crear_plato("Pizza muzzarela", 8000, ["Queso muzzarela", "Salsa de tomate", "Orégano", "Aceitunas"])
crear_plato("Pizza fugaseta", 8000, ["Queso", "Salsa de tomate", "Cebolla"])
crear_plato("Pizza especial", 9000, ["Queso", "Salsa de tomate", "Panceta", "Salchicha"])

def mostrar_platos():
    print("---")
    print()

    if not platos:
        pass

    else:
        for plato in platos:
            print(f"{plato.nombre} - ${plato.precio}")
            print(f"Ingredientes: {', '.join(plato.ingredientes)}")
            print("---")

    print()
    print("---")

def mostrar_plato(nombre:str):
    print("---")
    print()

    for plato in platos:
        if plato.nombre.replace(" ", "").strip().lower() == nombre.replace(" ", "").strip().lower():
            print("---")
            print(f"{plato.nombre} - ${plato.precio}")
            print(f"Ingredientes: {', '.join(plato.ingredientes)}")
            print("---")

    print()
    print("---")

def obtener_plato(nombre:str):
    for plato in platos:
        if plato.nombre.replace(" ", "").strip().lower() == nombre.replace(" ", "").strip().lower():
            return plato

    return None

def ordenar_pedido(info_pedido:dict):
    with open(f"Pedido para {info_pedido['nombre_cliente'].strip() + " " + info_pedido['apellido_cliente'].strip()}.pedido", "w") as pedido:
        pedido.write(f"{info_pedido['nombre_cliente'].strip()}\n")
        pedido.write(f"{info_pedido['apellido_cliente'].strip()}\n")
        pedido.write(f"{info_pedido['prioridad'].strip().lower()}\n")
        pedido.write(f"{info_pedido['plato_ordenado'].nombre}")

    print(f"Pedido creado para {info_pedido['nombre_cliente']}, ¡¡¡su pedido llega en un momento!!!")