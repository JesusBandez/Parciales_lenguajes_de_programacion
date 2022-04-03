"""Autor: Jesus Bandez. 1710046
Modulo que implementa la clase 'Client' que interactua con la clase 'VM' del
manejador de memoria"""

import re
from src.VM import VM

class Client(object):

    def __init__(self):
        """Clase que permite interactuar con la VM por medio de sus comandos"""
        self.VM = VM()
        print("Bienvenido al simulador de manejo de memoria dinamica!\n"
        " El manejador está construido usando lápidas.\n Comandos:\n"
        "RESERVAR <nombre> <valor>\nASIGNAR <nombre1> <nombre2>\n"
        "LIBERAR <nombre>\nIMPRIMIR <nombre>\nSALIR ")

    def loop(self):
        """Loop principal del cliente"""
        while True:
            self.interpretar_comando(input('< client > ').strip())

    def interpretar_comando(self, comando:str):
        """Recibe una string que representa un comando y lo interpreta"""
            
        if comando == '':
            pass

        elif re.match(r'^RESERVAR($| )', comando):
            self.reservar(comando)

        elif re.match(r'^ASIGNAR($| )', comando):
            self.asignar(comando)

        elif re.match(r'^LIBERAR($| )', comando):
            self.liberar(comando)

        elif re.match(r'^IMPRIMIR($| )', comando):
            self.imprimir(comando)


        elif re.match(r'^SALIR($| )', comando):
            self.salir()
            
        else:
            print("No se ha reconocido el comando")

    def reservar(self, comando:str):
        """Prepara el comando separando los parametros y se los pasa
            a la VM para reservar un nuevo apuntador """

        parametros = re.sub(r'^RESERVAR', '', comando).strip().split()
        if len(parametros) == 2:
            self.VM.reservar(*parametros)
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <nombre> <valor>')

    def asignar(self, comando):
        """Metodo que prepara el comando separando los parametros y se los pasa
         a la VM para asignar un apuntador a otro """

        parametros = re.sub(r'^ASIGNAR', '', comando).strip().split()
        if len(parametros) == 2:
            self.VM.asignar(*parametros)
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <nombre1> <nombre2>')

    def liberar(self, comando):
        """Metodo que prepara el comando separando los parametros y se los pasa
         a la VM para liberar a un apuntador """

        parametros = re.sub(r'^LIBERAR', '', comando).strip().split()
        if len(parametros) == 1:
            self.VM.liberar(*parametros)
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <nombre>')

    def imprimir(self, comando):
        """Metodo que prepara el comando separando los parametros y se los pasa
         a la VM para mostrar los valores de un apuntador"""

        parametros = re.sub(r'^IMPRIMIR', '', comando).strip().split()
        if len(parametros) == 1:
            self.VM.imprimir(*parametros)
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <nombre>')
     

    def salir(self):
        """Metodo para salir del cliente"""
        print('Hasta luego!')
        exit() 

if __name__== "__main__":
    client = Client()
    client.loop()
