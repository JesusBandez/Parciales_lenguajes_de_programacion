""" Autor: Jesus Bandez 17-10046
Clase que implementa la Virtual Machine encargada de manipular la
tabla de simbolos que contiene las clases """

from src.Tipos import Tipo
import src.mensajes as msg
class VM(object):
    
    def __init__(self):
        """Se inicializa con un diccionario que hace de una tabla de simbolos.
        Las claves corresponden al nombre de la clase y el valor es un objeto
        de la clase Tipo.  """
        self.tabla_de_simbolos: dict[str, Tipo] = {}
        

    def define_class(self, clase: str, superclase:str, metodos: list[str]):
        """ Metodo para definir una nueva clase

            Recibe:
                clase: String con el nombre de la clase
                superclase: String con el nombre de la superclase de la que 
                    hereda la clase. Puede ser None para representar que no 
                    hereda de nadie.
                metodos: Lista de string que contiene los metodos a definir
                    para la clase        
        """
        # Si ya existe la clase en la tabla de simbolos, no se hace nada
        if clase in self.tabla_de_simbolos:
            print(msg.clase_ya_definida(clase))
            return

        # Si la clase hereda de una superclase y la superclase no existe, 
        # no se hereda nada.
        if superclase and not superclase in self.tabla_de_simbolos:
            print(msg.superclase_no_definida(superclase))
            return

        # Si hay metodos repetidos en la lista de clase, no se hace nada.
        if len(metodos) != len(set(metodos)):
            print(msg.elementos_duplicados_en_lista_de_metodos(metodos))
            return

        # Si la clase a crear no hereda de nada
        if not superclase:
            # Se crea un nuevo elemento en la tabla de simbolos
            self.tabla_de_simbolos[clase] = Tipo(clase, None, metodos)
            print(msg.clase_creada(clase))
        else:
            # Si la nueva clase hereda
            self.tabla_de_simbolos[clase] = Tipo(
                clase, self.tabla_de_simbolos[superclase], metodos)                
            print(msg.clase_creada(clase, superclase))

    def describir(self, clase:str):
        """ Metodo que muestra todos los metodos de una clase por asociacion
            dinamica.
            Recibe:
                clase: String con el nombre de la clase a describir
        """
        # Si la clase no se ha creado, no se hace nada
        if not clase in self.tabla_de_simbolos:
            print(f"La clase {clase} no se encuentra definida")
            return

        # Se itera desde los metodos de la clase actual hasta los
        # metodos de las superclases. Se obtienen los metodos de 
        # las clases superiores dependiendo de si una subclase 
        # no lo ha sobreescrito.
        lista_de_metodos_con_tipo: tuple(str, str) = []
        historial_de_metodos: list(str) = []
        clase: Tipo = self.tabla_de_simbolos[clase]
        # Iterar por toda la jerarquia de clases
        while clase:
            # Lista que guarda los metodos de la clase y a que clase
            # corresponde
            lista_de_metodos_de_clase = []
            for metodo in clase.metodos:
                # Si el metodo de la clase actual existe en el historial
                # entonces una subclase lo definio.
                if metodo in historial_de_metodos:
                    continue

                lista_de_metodos_de_clase.append((metodo, clase.nombre))
                historial_de_metodos.append(metodo)
            
            # Se agregan los elementos de la lista conseguida en la primera
            # posicion de la lista.
            lista_de_metodos_con_tipo[0:0] = lista_de_metodos_de_clase
            clase = clase.super_clase

        # Se iteran por los metodos conseguidos desde la clase más alta
        # en la jerarquía hasta la más baja y se van imprimiendo los metodos.
        # Primero se imprimen aquellos que no fueron redefinidos por las 
        # subclases y luego se imprimen los de las subclases hasta llegar
        # a la clase que se pidió describir.
        print(msg.mostrar_metodos_y_clases(lista_de_metodos_con_tipo), end="")

        








