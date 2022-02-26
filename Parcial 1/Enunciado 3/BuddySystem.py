""" Autor: Jesus Bandez. 1710046
Modulo que implementa el manejo de memoria por medio del sistema BuddySistem en python"""

import math

class BuddySystem(object):
    
    def __init__(self, numero_de_bloques: int):
        """ Clase que implementa el sistema buddy system.
        Recibe:
            numero_de_bloques: cantidad de bloques que manejara el sistema. Este numero debe ser
            potencia de 2. En caso de no serlo, el programa toma la potencia de 2 mas cercana
        """
        # Diccionario de {str:Bloque} que lleva los bloques ocupados
        self.bloques_ocupados = {}


        self.cantidad_de_bloques = math.floor(math.log2(numero_de_bloques))

        # Se crea una lista de listas vacias de tamanaio log base 2 de numero_de_bloques
        self.lista_memoria_libre = [ [] for i in range(self.cantidad_de_bloques+1)]

        # Se agrega a la lista de mayor tamanaio el bloque inicial
        self.lista_memoria_libre[len(self.lista_memoria_libre)-1].append(Bloque(0, 2**self.cantidad_de_bloques -1))

    def reservar(self, nombre:str, cantidad:int):
        """ Metodo de la clase que permite reservar memoria en el sistema
            Recibe:
                nombre: nombre que se le quiere asignar al bloque
                cantidad: cantidad de memoria que se le asigna al bloque
        """
        if nombre in self.bloques_ocupados.keys():
            return (f'El nombre {nombre} ya esta en uso')
            

        # Se calcula la posicion en la lista libre donde debe ir el bloque
        pos_de_bloque = math.ceil(math.log2(cantidad))
        
        # Si la lista tiene bloques libres, entonces se usa uno de ellos.
        if len(self.lista_memoria_libre[pos_de_bloque])>0:
            bloque = self.lista_memoria_libre[pos_de_bloque].pop(0)

            self.bloques_ocupados[nombre] = bloque
            return(f'Se ha alojado la memoria en el bloque {bloque}')
            

        # Si la lista no tiene bloques libres, se itera hacia los bloques de 
        # mayor tamanio en busqueda de uno libre
        i = pos_de_bloque+1

        while (i != len(self.lista_memoria_libre)):

            if len(self.lista_memoria_libre[i]) > 0:                
                break

            i+=1

        # Si se tiene que i es el mismo que el tamanio de la lista, entonces no hay
        # memoria libre para reservar
        if (i == len(self.lista_memoria_libre)):
            return(f'No hay memoria libre suficiente para alojar al bloque')
            

        # Si no lo es, hay memoria libre. Se empieza a dividir el bloque conseguido
        # hasta que sea del tamanio necesario
        bloque_a_dividir = self.lista_memoria_libre[i].pop(0)

        while (i-1 >= pos_de_bloque):

            # Se crean los nuevos bloques que nacen de dividir al bloque mayor
            bloque0, bloque1 = bloque_a_dividir.dividir()
             
             # Agregar uno de los bloques a la lista
            self.lista_memoria_libre[i-1].append(bloque1)

            # Seguir dividiendo el bloque si es necesario
            bloque_a_dividir = bloque0
            i-=1

        # Se agrega el bloque final a los ocupados
        self.bloques_ocupados[nombre] = bloque_a_dividir

        return(f'Se ha alojado la memoria en el bloque {bloque_a_dividir}')

    
    def liberar(self, nombre:str):
        """Metodo que permite liberar un bloque que este ocupado en memoria
            Recibe: 
                nombre: str con el nombre del bloque a liberar
        """
        # Buscar el bloque a liberar
        bloque_a_liberar = self.bloques_ocupados.get(nombre, None)

        if not bloque_a_liberar:
            return(f'No hay un bloque con memoria alojada de nombre: {nombre}')
                    

        # Agregar el bloque a su respectiva lista
        pos_de_bloque = math.ceil(math.log2(bloque_a_liberar.capacidad))
        self.lista_memoria_libre[pos_de_bloque].append(bloque_a_liberar)

        self.fundir_bloques(bloque_a_liberar)

        self.bloques_ocupados.pop(nombre)
        return(f"Se ha liberado de memoria el bloque: {nombre} {bloque_a_liberar}")

    def fundir_bloques(self, bloque_a_fundir):
        """ Funcio recursiva que une los bloques segun estos se puedan combinar con su
        companiero. Una vez se unen dos bloques en uno de capacidad doble, se intenta seguir
        uniendo los otros bloques
        
            Parametros:
                bloque_a_fundir: Es el bloque que se intenta unir con su buddy

        """

        if not bloque_a_fundir:
            return
        else:
            # Conseguir la lista que correponde al tamanio del bloque
            pos_de_bloque = math.ceil(math.log2(bloque_a_fundir.capacidad))

            # Se consigue el numero del buddy de el bloque recien agregado
            numero_buddy = bloque_a_fundir.inicio() / bloque_a_fundir.capacidad

            if numero_buddy%2 != 0:
                direccionI_buddy = bloque_a_fundir.inicio() - bloque_a_fundir.capacidad
            else:
                direccionI_buddy = bloque_a_fundir.inicio() + bloque_a_fundir.capacidad

            bloque_fundido = None
            # Se busca en la lista libre de bloques de capacidad igual si el buddy esta en ella
            for index, bloque in enumerate(self.lista_memoria_libre[pos_de_bloque]):
                if bloque.inicio() == direccionI_buddy:
                    # Si el buddy existe, entonces se crea un nuevo bloque de ese tamanio y se 
                    # agrega a la lista de tamanio mayor

                    if numero_buddy % 2 == 0:
                        bloque_fundido = Bloque(bloque_a_fundir.inicio(), bloque.fin())
                        self.lista_memoria_libre[pos_de_bloque+1].append(bloque_fundido)
                    
                    else:
                        bloque_fundido = Bloque(bloque.inicio(), bloque_a_fundir.fin())
                        self.lista_memoria_libre[pos_de_bloque+1].append(bloque_fundido)
                    
                    self.lista_memoria_libre[pos_de_bloque].pop()
                    self.lista_memoria_libre[pos_de_bloque].pop(index)
                    break
            
            self.fundir_bloques(bloque_fundido)
        
        
    def mostrar(self):
        """Metodo que retorna una string con la forma actual en que se tienen reservado los bloques
        de memoria, los libres y la correspondencia entre los nombres y los bloques ocupados. Tanto
        los bloques ocupados como los libres se imprimen de forma ordenada
        """
        
        # Obtener todos los bloques libres y ordenar la lista de bloques libres
        bloques_libres = []
        for lista in self.lista_memoria_libre:
            bloques_libres.extend(lista)

        bloques_libres.sort(key=lambda x: x.inicio())

        out = ''
        # Imprimir la lista de bloques libres
        out += 'Bloques libres en memoria:\n'
        for bloque in bloques_libres:
            out += f'{bloque} '

        out += '\n\n'

        # Obtener todos los bloques ocupados y ordenar la lista de bloques libres
        bloques_ocupados = list(self.bloques_ocupados.values())
        bloques_ocupados.sort(key=lambda x: x.inicio())

        out+= 'Bloques ocupados en memoria:\n'
        for bloque in bloques_ocupados:
            out += f'{bloque} '
        out += '\n\n'
        
        # Imprimir la correspondecia nombre:bloque
        out += 'Correspondencia nombre:bloque\n'
        for key in list(self.bloques_ocupados.keys()):
            out+= f'"{key}":{self.bloques_ocupados[key]}  '
        out += '\n'

        return out



class Bloque(object):
    """Clase que representa un bloque de memoria."""

    def __init__(self, direccionI:int, direccionF:int):
        """ Representacion de un bloque de memoria. 
            RecibeÑ
                direccionI: La primera direccion que pertenece al bloque
                direccionF: La ultima direccion que pertenece al bloque
                 """

        self.rango_de_direcciones = (direccionI, direccionF)

        # Se calcula la capacidad por medio de las direcciones
        self.capacidad = direccionF - direccionI + 1

    def inicio(self):
        "Retorna la primera direccion del bloque"
        return self.rango_de_direcciones[0]

    def fin(self):
        "Retorna la ultima direccion del bloque"
        return self.rango_de_direcciones[1]

    def dividir(self):
        """Metodo que divide a un bloque en otros dos con igual capacidad. Donde la 
        primera direccion de uno inicia justo despues de la direccion del otro
            Retorna:
                BloqueA que inicia en la primera direccion del bloque dividio y termina
                    en la direccion a mitad del bloque
                BloqueB que inicia en la direccion a mitad del bloque dividido mas 1. Y, termina
                    en la direccion final del bloque dividido
                    """
        direccion_mediaI = self.inicio() + ((self.fin()-self.inicio())//2)
        direccion_mediaF = self.inicio() + ((self.fin()-self.inicio() + 1) //2)

        return Bloque(self.inicio(), direccion_mediaI), Bloque(direccion_mediaF, self.fin())

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f'{self.rango_de_direcciones}'
        