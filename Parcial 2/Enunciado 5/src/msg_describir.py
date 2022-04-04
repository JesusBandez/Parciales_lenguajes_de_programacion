"""Modulo con los mensajes de descripcion para el comando DESCRIBIR de la VM"""

def describir(ocupacion:int, alineacion:int, desperdicio:int):
    print(f"Tamaño total: {ocupacion}, Alineacion: {alineacion}, Desperdicio: {desperdicio}\n")

def describir_empaquetamiento_completo(ocupacion:int, alineacion:int, desperdicio:int):
    print("Si el lenguaje guarda registros y arreglos empaquetados")
    describir(ocupacion, alineacion, desperdicio)

def describir_empaquetamiento_solo_de_registros(ocupacion:int, alineacion:int, desperdicio:int):
    print("Si el lenguaje guarda registros empaquetados y arreglos sin empaquetar")
    describir(ocupacion, alineacion, desperdicio)

def describir_sin_empaquetamiento(ocupacion:int, alineacion:int, desperdicio:int):
    print("Si el lenguaje guarda sin empaquetamiento")
    describir(ocupacion, alineacion, desperdicio)

def describir_reordenando_campos(ocupacion:int, alineacion:int, desperdicio:int):
    print("Si el lenguaje reordena los campos")
    describir(ocupacion, alineacion, desperdicio)