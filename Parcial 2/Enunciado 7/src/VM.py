"""Clase que implementa la Virtual Machine encargada de manipular los
apuntadores del sistema manejador de memoria """

class VM(object):
    
    def __init__(self):
        """ Se inicializa la VM sin ningun apuntador ni ninguna lápida"""
        self.apuntadores = {}

        self.numero_de_lapidas = 0
        self.lapidas = {}
        

    def reservar(self, nombre: str, valor:str):
        """ Se define un nuevo apuntador con el nombre "nombre" y este 
        apunta a "valor"
            Recibe:
                nombre: String con el nombre del nuevo apuntador
                valor: String con el valor apuntador
        """
        # Se crea una nueva lapida y se le asigna el valor "valor"
        self.lapidas[self.numero_de_lapidas] = valor

        # El nuevo apuntador apunta a la lapida recien creada
        self.apuntadores[nombre] = self.numero_de_lapidas
        self.numero_de_lapidas += 1

        print(f'Se reservó "{nombre}" con valor "{valor}"')

    
    def asignar(self, nombre1:str, nombre2:str):
        """ Asigna al puntador nombre1 el apuntador nombre2
            Recibe:
                nombre1: nombre del apuntador a reasignar
                nombre2: nombre del apuntador al que le crean un alias
        """

        # Si no existen los apuntadores, se indica y no se hace nada
        if self.apuntadores.get(nombre1) is None:
            print(f'No existe el apuntador "{nombre1}"')
            return

        if self.apuntadores.get(nombre2) is None:
            print(f'No existe el apuntador "{nombre2}"')
            return

        # El apuntador nombre1 apunta a la lápida del apuntador nombre2
        self.apuntadores[nombre1] = self.apuntadores[nombre2]
        print(f'Se asignó "{nombre2}" a "{nombre1}"')
        
    def liberar(self, nombre:str):
        """ Libera el espacio ocupador por el apuntador nombre
            Recibe:
                nombre: Nombre del apuntador a liberar
        """

        # Se comprueba que exista el apuntador
        if self.apuntadores.get(nombre) is None:
            print(f'No existe el apuntador "{nombre}"')
            return

        # De existir el apuntador, se hace que la lapida apuntada por
        # él tome un valor centinela (None en este caso)
        self.lapidas[self.apuntadores[nombre]] = None

        print(f"Se liberó {nombre}")

    def imprimir(self, nombre:str):
        """ Imprime el valor asignado al apuntador "nombre"
            Recibe:
                nombre: nombre del apuntador a imprimir su valor
        """

        # Si no existe el apuntador, se notifica y no se hace nada
        if self.apuntadores.get(nombre) is None:
            print(f'ERROR, el nombre "{nombre}" no apunta a un valor válido')
            return

        # Se consigue la lapida apuntada por el apuntador.
        valor = self.lapidas[self.apuntadores[nombre]]
        # Si la lapida no contiene al valor centinela, entonces se imprime el
        # valor de la lapida. En caso contrario, el apuntador no apunta a un
        # a un valor valido
        if valor:
            print(valor)
        else:
            print(f'ERROR, el nombre "{nombre}" no apunta a un valor válido')
        








