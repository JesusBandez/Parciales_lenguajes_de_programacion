"""Autor: Jesus Bandez
Modulo que contiene los mensajes impresos por la VM"""

def clase_ya_definida(clase:str):
    return f"La clase \"{clase}\" ya se encuentra definida."

def superclase_no_definida(superclase:str):
    return (f"La clase \"{superclase}\" no se encuentra definida."
        " No puede ser usada como superclase si no se ha definido.")

def elementos_duplicados_en_lista_de_metodos(metodos: list[str]):
    return (f"Hay elementos duplicados en la lista de metodos:\n{metodos}"
        "\nNo pueden haber metodos duplicados.")

def clase_creada(clase:str , superclase:str=None):
    if superclase:
        return f"Se ha creado la clase \"{clase}\" que hereda de \"{superclase}\"."
    else:
        return f"Se ha creado la clase \"{clase}\"."

def mostrar_metodos_y_clases(lista_de_metodos_y_tipos: list[tuple[str, str]]):
    out = ''
    for metodo, clase in lista_de_metodos_y_tipos:
            out += f'{metodo} -> {clase} :: {metodo}\n'
    return out