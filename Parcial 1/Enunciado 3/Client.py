"""Autor: Jesus Bandez. 1710046
Modulo que implementa la clase 'Client' que interactua con la clase 'BuddySystem'"""

import re
import sys

from BuddySystem import BuddySystem

class Client(object):

    def __init__(self, bloques):
        """Clase que permite interactuar con el buddy system por medio de sus comandos"""

        self.buddy_system = BuddySystem(bloques)
        print('Bienvenido al emulador de BuddySystem!\n')
        print('Los comandos validos son:\nRESERVAR <nombre> <cantidad>  Ej: RESERVAR hi 3')
        print('LIBERAR <nombre>  Ej: LIBERAR hi')
        print('MOSTRAR')
        print('SALIR')
        print('\nautor: Jesus Bandez')

    def loop(self):
        """Loop principal del cliente. Se reciben los argumentos por medio de la terminal"""
        while True:
            
            comando:str = input('< client > ').strip()
            if comando == '':
                pass

            elif re.match(r'^RESERVAR($| )', comando):
                self.reservar(comando)

            elif re.match(r'^LIBERAR($| )', comando):
                self.liberar(comando)

            elif re.match(r'^MOSTRAR($| )', comando):
                self.mostrar()

            elif re.match(r'^SALIR($| )', comando):
                self.salir(comando)
                
            else:
                print("No se ha reconocido el comando")

    def reservar(self, comando:str):
        """Metodo que prepara el comando separando los parametros y se los pasa al BuddySystem ejecutando
        el metodo reservar """

        parametros = re.sub(r'^RESERVAR', '', comando).strip().split()

        if len(parametros) == 2:
            try:
                cantidad = int(parametros[1])
            except:
                print(f'Error en accion: "{comando}"')
                print(f'No se puede convertir a entero la cantidad a reservar: "({parametros[1]})"')
                return
            print(self.buddy_system.reservar(parametros[0], cantidad))
        
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos <nombre> <cantidad>')
            print(f'Se recibieron: {len(parametros)} argumentos')

    def liberar(self, comando:str):
        """Metodo que prepara el comando separando los parametros y se los pasa al BuddySystem ejecutando
        el metodo liberar """
        parametros = re.sub(r'^LIBERAR', '', comando).strip().split()

        if len(parametros) == 1:
            print(self.buddy_system.liberar(parametros[0]))
        else:
            print(f'Error en accion: "{comando}"\nSe requiere el argumento: <nombre>')
            print(f'Se recibieron: {len(parametros)} argumentos')

    def mostrar(self):
        """Metodo para ejecutar la funcion 'mostrar' del buddysystem"""
        print(self.buddy_system.mostrar())

    def salir(self, comando:str):
        """Metodo para salir del cliente"""
        print('Hasta luego!')
        exit()

# Importar con argumentos
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\n\n\nDebe pasar como argumento la cantidad de memoria para inicializar el cliente con")
        print(".> python Client.py <cantidadDeMemoria>\n")
    
    else:
        try:
            cantidad = int(sys.argv[1])
        except:
            print("Cantidad de memoria invalida pasada como argumento.")

        cliente = Client(cantidad)
        cliente.loop()