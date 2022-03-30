"""Autor: Jesus Bandez. 1710046
Modulo que implementa la clase 'Client' que interactua con la clase 'VM'"""


from http import client
import re
from src.VM import VM

class Client(object):

    def __init__(self):
        """Clase que permite interactuar con la VM por medio de sus comandos"""
        self.VM = VM()


    def loop(self):
        """Loop principal del cliente"""
        while True:
            
            comando:str = input('< client > ').strip()
            if comando == '':
                pass

            elif re.match(r'^EVAL($| )', comando):
                self.eval(comando)

            elif re.match(r'^MOSTRAR($| )', comando):
                self.mostrar(comando)

            elif re.match(r'^SALIR($| )', comando):
                self.salir()
                
            else:
                print("No se ha reconocido el comando")

    def eval(self, comando:str):
        """Prepara el comando separando los parametros y se los pasa
            a la VM para evaluar la expresion """

        parametros = re.sub(r'^EVAL', '', comando).strip()

        if re.match(r'^PRE', parametros):

            print(self.VM.eval('PRE', re.sub(r'^PRE', '', parametros).strip()))
        
        elif re.match(r'^POST', parametros):

            print(self.VM.eval('POST', re.sub(r'^POST', '', parametros).strip()))
        
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
            ' <orden> <expr>')

    def mostrar(self, comando):
        """Metodo que prepara el comando separando los parametros y se los pasa
         a la VM para mostrar la expresion en notacion infija """

        parametros = re.sub(r'^MOSTRAR', '', comando).strip()
    
        if re.match(r'^PRE', parametros):

            print(self.VM.mostrar('PRE', re.sub(r'^PRE', '', parametros).strip()))
        
        elif re.match(r'^POST', parametros):

            print(self.VM.mostrar('POST', re.sub(r'^POST', '', parametros).strip()))
        
        else:
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
            ' <orden> <expr>')

     

    def salir(self):
        """Metodo para salir del cliente"""
        print('Hasta luego!')
        exit() 

if __name__== "__main__":
    client = Client()
    client.loop()
