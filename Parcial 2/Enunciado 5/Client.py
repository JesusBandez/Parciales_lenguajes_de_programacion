"""Autor: Jesus Bandez. 1710046
Modulo que implementa la clase 'Client' que interactua con la clase 'VM' del
manejador de memoria de tipos atomicos, registros y arreglos"""

import re
from src.VM import VM

class Client(object):

    def __init__(self):
        """Clase que permite interactuar con la VM por medio de los comandos"""
        self.VM = VM()
        print("Bienvenido al majeador de memoria de tipos atomicos, registros y"
        " arreglos!\nComandos validos:\nATOMICO <nombre> <representacion> "
        "<alineacion>\nSTRUCT <nombre> [<tipo>]\nARREGLO <nombre> <tipo> <tamaño>\n"
        "DESCRIBIR <nombre>\nSALIR")

    def loop(self):
        """Loop principal del cliente"""
        while True:
            self.interpretar_comando(input('< client > ').strip())

    def interpretar_comando(self, comando:str):
        """Recibe una string que representa un comando y lo interpreta"""
            
        if comando == '':
            pass

        elif re.match(r'^ATOMICO($| )', comando):
            self.atomico(comando)

        elif re.match(r'^STRUCT($| )', comando):
            self.struct(comando)

        elif re.match(r'^ARREGLO($| )', comando):
            self.arreglo(comando)

        elif re.match(r'^DESCRIBIR($| )', comando):
            self.describir(comando)


        elif re.match(r'^SALIR($| )', comando):
            self.salir()
            
        else:
            print("No se ha reconocido el comando")

    def atomico(self, comando:str):
        """ Recibe un comando y preparar los parametros para pasarlos a la VM
            El comando debe cumplir con la estructura:
            ATOMICO <nombre> <representacion> <alineacion>
            Por ejemplo:
            ATOMICO atomo 4 6
        """

        parametros = re.sub(r'^ATOMICO', '', comando).strip().split()

        if len(parametros) != 3:         
            print(f'Error en accion: "{comando}"\nSe requieren los argumentos'
                ' <nombre> <representacion> <alineacion>')
            return

        if not re.match('^[A-Za-z0-9]+$', parametros[0]):
            print(f'Error en accion: "{comando}"\nNombre invalido en {parametros[0]}'
            ' debe ser un nombre alfanumerico')

        else:
            try:
                parametros[1] = int(parametros[1])                
                parametros[2] = int(parametros[2])
                assert parametros[1] > 0 and parametros[2] > 0

            except:
                print("Los argumentos <representacion> y <alineacion>"
                " deben ser numeros enteros mayores a 0")
                return

            self.VM.atomico(*parametros)
            
        

    def struct(self, comando):
        """ Recibe un comando y preparar los parametros para pasarlos a la VM
            El comando debe cumplir con la estructura:

            STRUCT <nombre> [<tipo>] 

            donde [<tipo>] es una lista de <tipos>. 
            Por ejemplo:

            STRUCT hola [tipo1 tipo2 tipo3]"""

        parametros = re.sub(r'^STRUCT', '', comando).strip()

        foo = re.match(r'^[A-Za-z0-9]+($| )', parametros)
        if not foo:
            print(f'Error en accion: "{comando}"\nSe requiere el argumento'
                ' <nombre>, y debe ser alfanumerico')
            return

        nombre = foo.group(0).strip()
        tipos = parametros.lstrip(nombre).strip()


        if not re.match(r'^\[[A-Za-z0-9 ]+\]$', tipos):
            print(f'Sintaxis invalida en: "{comando}"')
            return

        tipos = tipos.strip('[]').split()

        if len(tipos) == 0:
            print(f'Error en accion: "{comando}"\nSe requiere que el argumento '
            '[<tipo>] sea una lista no vacia de tipos')
            return

        else:
            self.VM.struct(nombre, tipos)

        

    def arreglo(self, comando):
        """ Recibe un comando y prepara los parametros para pasarlos a la VM
            El comando debe cumplir con la estructura:
            ARREGLO <nombre> <tipo> <tamanio>
            Por ejemplo:
            ARREGLO cincoGatos gato 5
        """

        parametros = re.sub(r'^ARREGLO', '', comando).strip()

        foo = re.match(r'^[A-Za-z0-9]+($| )', parametros)
        if not foo:
            print(f'Error en accion: "{comando}"\nSe requiere el argumento'
                ' <nombre>, y debe ser alfanumerico')
            return

        parametros = parametros.split()

        try:
            parametros[2] = int(parametros[2])
            assert parametros[2] > 0
        except:
            print(f'Error en accion: "{comando}"\nSe requiere que el argumento'
                ' <tamaño> sea un numero entero mayor a 0')
            return
        
        self.VM.arreglo(*parametros)

        
    def describir(self, comando):
        """ Recibe un comando y prepara los parametros para pasarlos a la VM
            El comando debe cumplir con la estructura:
            DESCRIBIR <nombre>
            Por ejemplo:
            DESCRIBIR cincoGatos
        """

        parametros = re.sub(r'^DESCRIBIR', '', comando).strip()


        foo = re.match(r'^[A-Za-z0-9]+($| )', parametros)
        if not foo:
            print(f'Error en accion: "{comando}"\nSe requiere el argumento'
                ' <nombre>, y debe ser alfanumerico')
            return

        parametros = parametros.split()


        if len(parametros) != 1:
            print(f'Error en accion: "{comando}"\nSólo se requiere el argumento'
                ' <nombre>')
            return
        else:
            self.VM.describir(*parametros)

     

    def salir(self):
        """Metodo para salir del cliente"""
        print('Hasta luego!')
        exit() 

if __name__== "__main__":
    client = Client()
    client.loop()
