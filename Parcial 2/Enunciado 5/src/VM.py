""" """
import src.Atomo as Atomo
import src.Arreglo as Arreglo
import src.Struct as Struct
from src.Tipo import Tipo
import src.msg_describir as msg
import itertools

class VM(object):
    
    def __init__(self):
        """Se inicializan los diccionarios que contendran los atomos, arreglos
        y registros en la VM."""
        self.atomos = {}
        self.arreglos = {}
        self.registros = {}
        

    def atomico(self, nombre: str, representacion:int, alineacion:int):
        """ Se crea un nuevo atomo siempre que ya no exista un tipo de datos
        con mismo nombre asociado
            Recibe: 
                nombre: nombre del atomo a crear
                representacion: cantidad de memoria que ocupa
                alineacion: alineacion de memoria que requiere el atomo 
        """
        if self.atomos.get(nombre):
            print(f"ERROR: Ya existe el atomo {nombre}")
            return

        if self.arreglos.get(nombre):
            print(f"ERROR: Ya existe un arreglo con nombre {nombre}")
            return  

        if self.registros.get(nombre):
            print(f"ERROR: Ya existe un struct con el nombre {nombre}")
            return

        self.atomos[nombre] = Atomo.Atomo(nombre, representacion, alineacion)

    
    def struct(self, nombre:str, tipos:list[Tipo]):
        """ Se crea un nuevo registro siempre que ya no exista un tipo de datos
        con mismo nombre asociado y que ya existan todos los tipos en la lista
        de tipos
            Recibe: 
                nombre: nombre del registro a crear
                tipos: lista de strings que va a contener el registro. El orden
                    en que aparecen los tipos en la lista es el mismo que tendran
                    en el registro 
                
        """

        if self.atomos.get(nombre):
            print(f"ERROR: Ya existe un atomo de nombre {nombre}")
            return

        if self.arreglos.get(nombre):
            print(f"ERROR: Ya existe un arreglo con nombre {nombre}")
            return  

        if self.registros.get(nombre):
            print(f"ERROR: Ya existe el struct {nombre}")
            return

        for tipo in tipos:
            if not self.existe_el_tipo(tipo):
                print(f"ERROR: No existe el tipo {tipo}")
                return       

        self.registros[nombre] = Struct.Struct(nombre, tipos)
        
    def arreglo(self, nombre:str, tipo:str, tamanio:int):
        """ Se crea un nuevo arreglo siempre que ya no exista un tipo de datos
        con mismo nombre asociado     
            Recibe: 
                nombre: nombre del arreglo a crear
                tipo: tipo del arreglo 
                tamanio: el tamanio del arreglo
                
        """
        if self.atomos.get(nombre):
            print(f"ERROR: Ya existe un atomo de nombre {nombre}")
            return

        if self.arreglos.get(nombre):
            print(f"ERROR: Ya existe el arreglo {nombre}")
            return  

        if self.registros.get(nombre):
            print(f"ERROR: Ya existe un struct con nombre {nombre}")
            return

        if not self.existe_el_tipo(tipo):
            print(f"ERROR: No existe el tipo {tipo}")
            return

        self.arreglos[nombre] = Arreglo.Arreglo(nombre, tipo, tamanio)

    def describir(self, nombre:str):
        """ Ejecuta un conteo de la memoria ocupada por el tipo <nombre>
        bajo cuatro condiciones:
            Cuando se guardan los registros y arreglos sin empaquetar
            Cuando se guardan los registros empaquetados y arreglos sin empaquetar
            Cuando registros y arreglos se guardan empaquetados
            Cuando se reordenan los campos de manera optima
        """

        # Comprobar que existe el tipo
        tipo = self.buscar_el_tipo(nombre)
        if not tipo:
            print(f"ERROR: No existe el tipo {nombre}")
            return

        # Si se guardan con empaquetamiento para todo
        ocupacion = self.describir_con_empaquetamiento_completo(tipo)
        alineacion = self.calcular_alineacion_de_tipo(tipo)
        msg.describir_empaquetamiento_completo(ocupacion, alineacion, 0)

        # Si se guardan empaquetando los registros pero no los arreglos        
        (tamanio, desperdicio) = self.describir_con_empaquetamiento_de_registros(tipo)
        alineacion = self.calcular_alineacion_de_tipo(tipo)
        msg.describir_empaquetamiento_solo_de_registros(tamanio, alineacion, desperdicio)

        # Si se guardan sin ningun tipo de empaquetamiento
        (tamanio, desperdicio) = self.describir_sin_ningun_empaquetamiento(tipo)
        alineacion = self.calcular_alineacion_de_tipo(tipo)
        msg.describir_sin_empaquetamiento(tamanio, alineacion, desperdicio)

        # Si se guardan buscando la forma mas optima
        (tamanio, desperdicio) = self.describir_reordenando_los_campos(tipo)
        msg.describir_reordenando_campos(tamanio, alineacion, desperdicio)
  
    def describir_con_empaquetamiento_de_registros(self, tipo:Tipo) -> tuple[int, int]:
        """Se calcula el peso total y el desperdicio si se empaquetan los arreglos"""
        return self.calcular_index_y_desperdicio_empaquetando_registros(0, 0, tipo)

    def describir_con_empaquetamiento_completo(self, tipo:Tipo) -> tuple[int, int]:
        """Cuando se empaqueta todo el contenido de un tipo, entonces no hay
        desperdicio y su tamanio es el peso total del tipo"""
        return self.calcular_ocupacion_de_tipo(tipo)

    def describir_sin_ningun_empaquetamiento(self, tipo:Tipo) -> tuple[int, int]:
        """Se calcula el peso total y el desperdicio si nada se empaqueta"""
        return self.calcular_index_y_desperdicio(0, 0, tipo)

    def describir_reordenando_los_campos(self, tipo:Tipo) -> tuple[int, int]:
        """Se calcula TODAS las posibles permutaciones del campo del registro
            y se retorna la menor memoria ocupada y desperdiciada posible"""
        return self.calcular_con_reordenacion(0, 0, tipo)

    def calcular_con_reordenacion(self, index:int, desperdicio_total:int, tipo:Tipo):
        """ Metodo recursivo que calcula la memoria y el desperdicio usado por un tipo.
            En caso de ser un registro, se calculan cuanta memoria ocuparian sus campos 
            en todas las permutaciones posibles. Luego, se retorna la menor memoria ocupada
            Recibe:
                index: Representa el "indice" actual de memoria ocupada.
                desperdicio_total: Es el desperdicio de memoria calculado actualmente
                tipo: El tipo a calcular su desperdicio y memoria ocupada.
            Retorna: Tupla de enteros donde el primer elemento es la memorica ocupada y
                    el segundo es el desperdicio total
        """
        if isinstance(tipo, Atomo.Atomo):
            # El desperdicio de un atomo es lo que le "falta" para poder estar alineado
            # en memoria 
            desperdicio_local = self.calcular_desperdicio(
                            index, self.calcular_alineacion_de_tipo(tipo))

            # Se suma el desperdicio al total
            desperdicio_total += desperdicio_local

            # Se calcula lo que debe costar el atomo en memoria
            index += desperdicio_local + tipo.representacion

            # Se retorna la memoria ocupada y el desperdicio total        
            return (index, desperdicio_total)

        elif isinstance(tipo, Arreglo.Arreglo):
            # Se calcula la memoria desperdiciada para poder alinear
            # el arreglo
            alineacion = self.calcular_alineacion_de_tipo(tipo)            
            desperdicio_local = self.calcular_desperdicio(index, alineacion)

            # Se suma al desperdicio total la memoria desperdiciada
            desperdicio_total += desperdicio_local

            # Se aumenta el indice actual de memoria usada
            index += (desperdicio_local + self.calcular_ocupacion_de_tipo(
                                        self.buscar_el_tipo(tipo.tipo))
                                  * tipo.tamanio)

            return (index, desperdicio_total)

        else:
            # Crear una copia de la lista de campos
            campos_backup = tipo.tipos[:]
            # Copia de index actual y desperdicio total actual
            desperdicio_total_backup = desperdicio_total
            index_backup = index

            # Se consigue todas las permutaciones posibles de los campos del registro
            permutaciones_de_campos = list(itertools.permutations(tipo.tipos))
            resultados = []

            for permutacion in permutaciones_de_campos:
                # Se asigna la permutacion actual al tipo            
                tipo.tipos = permutacion

                # Se calcula la memoria y el desperdicio que deben tener los campos
                # de la estructura. Se inicializan en 0 porque se asume que la
                # estructura esta empaquetada
                (index_temp, desperdicio_temp) = (0, 0)
                for tipo_en_estructura in tipo.tipos:
                    (index_temp, desperdicio_temp) = (
                    self.calcular_con_reordenacion(
                                            index_temp, desperdicio_temp,
                                            self.buscar_el_tipo(tipo_en_estructura)))

                # Se suma el total de memoria ocupado por los campos de la estructura
                index += index_temp
                # Se suma el total de memoria desperdiciada por los campos de la estructura
                desperdicio_total += desperdicio_temp

                # Se guardan los resultados conseguidos
                resultados.append((index, desperdicio_total))

                # Se restauran el desperdicio total y la memoria ocupada
                desperdicio_total = desperdicio_total_backup
                index = index_backup

            # Se reasigna al tipo sus campos originales
            tipo.tipos = campos_backup

            # Se retorna la tupla con menor memoria ocupada
            return min(resultados)

    def calcular_index_y_desperdicio_empaquetando_registros(self, index:int , desperdicio_total:int , tipo:object) -> tuple[int, int]:
        """ Metodo recursivo que calcula la memoria y el desperdicio usado por un tipo pero
            teniendo en cuenta que se pueden empaquetar arreglos
            Recibe:
                index: Representa el "indice" actual de memoria ocupada.
                desperdicio_total: Es el desperdicio de memoria calculado actualmente
                tipo: El tipo a calcular su desperdicio y memoria ocupada.
            Retorna: Tupla de enteros donde el primer elemento es la memorica ocupada y
                    el segundo es el desperdicio total
        """
        if isinstance(tipo, Atomo.Atomo):
            # El desperdicio de un atomo es lo que le "falta" para poder estar alineado
            # en memoria 
            desperdicio_local = self.calcular_desperdicio(
                            index, self.calcular_alineacion_de_tipo(tipo))
            
            # Se suma el desperdicio al total
            desperdicio_total += desperdicio_local

            # Se calcula lo que debe costar el atomo en memoria
            index += desperdicio_local + tipo.representacion
            # Se retorna la memoria ocupada y el desperdicio total
            return (index, desperdicio_total)

        elif isinstance(tipo, Arreglo.Arreglo):
            # Se calcula la memoria desperdiciada para poder alinear
            # el arreglo
            alineacion = self.calcular_alineacion_de_tipo(tipo)            
            desperdicio_local = self.calcular_desperdicio(index, alineacion)

            # Se suma al desperdicio total la memoria desperdiciada
            desperdicio_total += desperdicio_local

            # Se aumenta el indice actual de memoria usada
            index += (desperdicio_local + self.calcular_ocupacion_de_tipo(
                                        self.buscar_el_tipo(tipo.tipo))
                                  * tipo.tamanio)

            return (index, desperdicio_total)

        else:
            # Se calcula la memoria y el desperdicio que deben tener los campos
            # de la estructura. Se inicializa la index_temp porque no se empaqueta
            # la estructura
            (index_temp, desperdicio_temp) = (0, 0)
            for tipo in tipo.tipos:

                (index_temp, desperdicio_temp) = (                    
                self.calcular_index_y_desperdicio_empaquetando_registros(
                    index_temp, desperdicio_temp, self.buscar_el_tipo(tipo)))

            # Se suma el total de memoria ocupado por los campos de la estructura
            index += index_temp
            # Se suma el total de memoria desperdiciada por los campos de la estructura
            desperdicio_total += desperdicio_temp

            return (index, desperdicio_total)

    def calcular_desperdicio(self, index:int, alineacion:int) -> int:
        desperdicio = alineacion - index % alineacion
        return desperdicio if index % alineacion != 0 else 0

    def calcular_index_y_desperdicio(self, index:int, desperdicio_total:int, tipo:Tipo):
        """ Metodo recursivo que calcula la memoria y el desperdicio usado por un tipo
            Recibe:
                index: Representa el "indice" actual de memoria ocupada.
                desperdicio_total: Es el desperdicio de memoria calculado actualmente
                tipo: El tipo a calcular su desperdicio y memoria ocupada. 
        """

        if isinstance(tipo, Atomo.Atomo):
            # El desperdicio de un atomo es lo que le "falta" para poder estar alineado
            # en memoria 
            desperdicio_local = self.calcular_desperdicio(
                            index, self.calcular_alineacion_de_tipo(tipo))

            # Se suma el desperdicio al total
            desperdicio_total += desperdicio_local

            # Se calcula lo que debe costar el atomo en memoria
            index += desperdicio_local + tipo.representacion

            # Se retorna la memoria ocupada y el desperdicio total
            return (index, desperdicio_total)

        elif isinstance(tipo, Arreglo.Arreglo):
            # Se calcula la memoria desperdiciada para poder alinear
            # el arreglo
            alineacion = self.calcular_alineacion_de_tipo(tipo)            
            desperdicio_local = self.calcular_desperdicio(index, alineacion)

            # Se suma al desperdicio total la memoria desperdiciada
            desperdicio_total += desperdicio_local

            # Se aumenta el indice actual de memoria usada
            index += (desperdicio_local + self.calcular_ocupacion_de_tipo(
                                        self.buscar_el_tipo(tipo.tipo))
                                  * tipo.tamanio)

            return (index, desperdicio_total)

        else:
            # Se alinia el registro con la memoria 
            alineacion = self.calcular_alineacion_de_tipo(tipo)
            desperdicio_local = self.calcular_desperdicio(index, alineacion)
            index += desperdicio_local
            desperdicio_total += desperdicio_local

            # Se calcula la memoria y el desperdicio que deben tener los campos
            # de la estructura 
            (index_temp, desperdicio_temp) = (0, 0)
            for tipo in tipo.tipos:
                (index_temp, desperdicio_temp) = self.calcular_index_y_desperdicio(
                                        index_temp, desperdicio_temp,
                                        self.buscar_el_tipo(tipo))

            # Se suma el total de memoria ocupado por los campos de la estructura
            # al igual que su desperdicio
            index += index_temp
            desperdicio_total += desperdicio_temp
            return (index, desperdicio_total)
                                 

    def calcular_ocupacion_de_tipo(self, tipo:Tipo) -> int:
        """Se calcula el tamanio total que ocupa el tipo ignorando las reglas
        de alineacion.
            Recibe:
                tipo: objeto que puede ser un Atomo, un Arreglo o una Struct
            Retorna:
                Un numero entero que representa la cantidad de memoria que ocupa
                el tipo
            
        """
        if isinstance(tipo, Atomo.Atomo):
            # La ocupacion de un atomo es su atributo representacion
            return tipo.representacion
        
        elif isinstance(tipo, Arreglo.Arreglo):
            # La ocupacion de un arreglo es la ocupacion de su tipo
            # multiplicada por su tamaño
            return tipo.tamanio * self.calcular_ocupacion_de_tipo(
                                        self.buscar_el_tipo(tipo.tipo))

        else:
            # La ocupacion de un registro es la suma de las ocupaciones de
            # sus campos
            return sum(
                [self.calcular_ocupacion_de_tipo(self.buscar_el_tipo(tipo)) 
                    for tipo in tipo.tipos])

    def calcular_alineacion_de_tipo(self, tipo:Tipo) -> int:
        """Funcion que calcula de manera recursiva la alineacion de un tipo
            Recibe:
                tipo: El tipo al que se le va a calcular su alineacion
            Retorna:
                Entero con la alineacion del tipo
        """        
        if isinstance(tipo, Atomo.Atomo):
            # La alineacion de un atomo es su atributo alineacion
            return tipo.alineacion
        
        elif isinstance(tipo, Arreglo.Arreglo):
            # La alineacion de un arreglo es la alineacion de su tipo
            return self.calcular_alineacion_de_tipo(
                                        self.buscar_el_tipo(tipo.tipo))
        else:
            # La alineacion de un registro es la alineacion del primer elemento
            # de sus campos
            return self.calcular_alineacion_de_tipo(self.buscar_el_tipo(tipo.tipos[0])) 
       
        
    def existe_el_tipo(self, tipo:str) -> bool:
        """Recibe el nombre de un tipo y retorna si existe en la VM
            Recibe:
                tipo: tipo a buscar en los diccionarios de la VM
            Retorna:
                True si existe el tipo, false en caso contrario
        """
        return (self.atomos.get(tipo) or self.arreglos.get(tipo) 
            or self.registros.get(tipo))

    def buscar_el_tipo(self, tipo:str) -> Tipo:
        """Recibe el nombre de un tipo y retorna si existe
            Recibe:
                tipo: nombre del tipo a buscar 
            Retorna:
                El tipo si se consigue, none en caso contrario
        """

        if self.atomos.get(tipo):
            return self.atomos[tipo]
        elif self.arreglos.get(tipo):
            return self.arreglos[tipo]
        elif self.registros.get(tipo):
            return self.registros[tipo]
        else:
            return None