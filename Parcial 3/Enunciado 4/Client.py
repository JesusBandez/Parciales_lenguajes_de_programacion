"""Autor: Jesus Bandez 1710046
Interprete que se encarga de despachar a la VM los comandos introducidos por
el usuario
"""

import re
from pytest import param
from src.VM import VM

class Client(object):

    def __init__(self):
        """Clase que permite interactuar con la VM por medio de sus comandos"""
        print("Bienvenido al manejador de tablas de metodos virtuales. Comandos:\n"
        "CLASS <tipo> [<nombre>] o CLASS <tipo> : <superclase> [<nombre>]\n"
        "DESCRIBIR <tipo>\nSALIR")
        self.VM = VM()

    def loop(self):
        """Loop principal del cliente"""
        while True:
            self.interpretar_comando(input('< client > ').strip())

    def interpretar_comando(self, comando:str):
        """Recibe una string que representa un comando y lo interpreta"""
            
        if comando == '':
            pass

        elif re.match(r'^CLASS($| )', comando):
            self.define_class(comando)

        elif re.match(r'^DESCRIBIR($| )', comando):
            self.describir(comando)

        elif re.match(r'^SALIR($| )', comando):
            self.salir()
            
        else:
            print("No se ha reconocido el comando")

    def define_class(self, comando:str):
        """ Recibe un comando y comprueba que sea valido para pasarlo al
        metodo define_class de la VM.
        """
        parametros = re.sub(r'^CLASS', '', comando).strip().split(":")

        # Si es posible separar en dos por medio del caracter ":", entonces
        # el comando contiene una definicion de clase con superclase
        if len(parametros) == 2:

            clase = parametros[0].strip()         
            # Se debe poder separar la parte derecha del comando en dos o mas 
            # partes. Se extrae la superclase y el resto son los metodos a 
            # definir para la clase   
            parametros = parametros[1].split()            
            if len(parametros) >= 2:
                superClase = parametros[0]
                metodos = parametros[1:]
            else:
                print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
                return
        
        # Si no se separa en dos, entonces no hay definicion con superclase
        elif len(parametros) == 1 and parametros[0].strip() != '':
            parametros = parametros[0].split()
            if len(parametros) >= 2:
                clase = parametros[0]
                superClase = None
                metodos = parametros[1:]
            else:
                print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
                return

        # Cualquier otro caso, es un error
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <tipo> [<nombre>] o <tipo> : <superclase> [<nombre>]')
            return
        
        self.VM.define_class(clase, superClase, metodos)        

    def describir(self, comando):
        """ Metodo que despacha un nombre a la VM para describir la clase
        """
        clase = re.sub(r'^DESCRIBIR', '', comando).strip()
        self.VM.describir(clase)

    def salir(self):
        """Metodo para salir del cliente"""
        print('Hasta luego!')
        exit() 

if __name__== "__main__":
    client = Client()
    client.loop()
