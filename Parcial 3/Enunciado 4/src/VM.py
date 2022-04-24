"""Clase que implementa la Virtual Machine encargada de manipular los
apuntadores del sistema manejador de memoria """

from src.Tipos import Tipo

class VM(object):
    
    def __init__(self):
        """ """
        self.tabla_de_simbolos: dict[str, Tipo] = {}
        

    def define_class(self, clase: str, superclase:str, metodos: list[str]):
        """ 
        """
        if clase in self.tabla_de_simbolos:
            print(f"La clase {clase} ya se encuentra definida")
            return            
        if superclase and not superclase in self.tabla_de_simbolos:
            print(f"La clase {superclase} no se encuentra definida")
            return

        if len(metodos) != len(set(metodos)):
            print(f"Hay elementos duplicados en la lista de metodos:\n{metodos}")
            return

        if not superclase:
            self.tabla_de_simbolos[clase] = Tipo(clase, None, metodos)
            print(f"Se ha creado la clase {clase}")
        else:
            self.tabla_de_simbolos[clase] = Tipo(clase, self.tabla_de_simbolos[superclase], metodos)
            print(f"Se ha creado la clase {clase} que hereda de {superclase}")

    def describir(self, clase:str):
        """ 
        """
        if not clase in self.tabla_de_simbolos:
            print(f"La clase {clase} no se encuentra definida")
            return

        lista_de_metodos_con_tipo: tuple(str, str) = []
        historial_de_metodos: list(str) = []
        clase: Tipo = self.tabla_de_simbolos[clase]
        while clase:
            lista_de_metodos_de_clase = []
            for metodo in clase.metodos:
                if metodo in historial_de_metodos:
                    continue

                lista_de_metodos_de_clase.append((metodo, clase.nombre))
                historial_de_metodos.append(metodo)
            
            lista_de_metodos_con_tipo[0:0] = lista_de_metodos_de_clase
            clase = clase.super_clase

        for metodo, clase in lista_de_metodos_con_tipo:
            print(f'{metodo} -> {clase} :: {metodo}')

        








