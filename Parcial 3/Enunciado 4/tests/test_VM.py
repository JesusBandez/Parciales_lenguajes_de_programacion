import os
import sys

sys.path.insert(1, os.path.abspath('.'))

import Client
import src.mensajes as msg
cliente = Client.Client()

def test_VM(capsys):
    # Pasar una string al metodo "interpretar_comando" es
    # equivalente a cuando el usuario escribe el comando
    # por la terminal y esta es pasada al cliente

    # Crear una nueva clase en la VM
    cliente.interpretar_comando('CLASS A x y z')
    captura_de_interprete = capsys.readouterr()
    # Simular salida
    print(msg.clase_creada('A'))
    captura_de_simulacion = capsys.readouterr()
    assert captura_de_interprete == captura_de_simulacion

    # Crea nueva clase con superclase A y que redefine z
    cliente.interpretar_comando('CLASS B : A s d z')
    captura_de_interprete = capsys.readouterr()
    # Simular salida
    print(msg.clase_creada('B', 'A'))
    captura_de_simulacion = capsys.readouterr()
    assert captura_de_interprete == captura_de_simulacion

    # Describir A
    cliente.interpretar_comando('DESCRIBIR A')
    captura_de_interprete = capsys.readouterr()
    # Simular salida
    print(msg.mostrar_metodos_y_clases([('x', 'A'), ('y', 'A'), ('z', 'A')]), end='')
    captura_de_simulacion = capsys.readouterr()
    assert captura_de_interprete == captura_de_simulacion

    # Describir B
    cliente.interpretar_comando('DESCRIBIR B')
    captura_de_interprete = capsys.readouterr()
    # Simular salida
    print(msg.mostrar_metodos_y_clases([('x', 'A'), ('y', 'A'), ('s', 'B'), ('d', 'B'), ('z', 'B')]), end='')
    captura_de_simulacion = capsys.readouterr()
    assert captura_de_interprete == captura_de_simulacion        

    # Comandos que intentan definir clases ya creadas o comandos mal usados que no afectan el programa
    cliente.interpretar_comando('CLASS A 2')
    cliente.interpretar_comando('CLASS C : D 3')
    cliente.interpretar_comando('CLASS C 2 2 2 2')
    cliente.interpretar_comando('DESCRIBIR C')

    # Comandos sin sentido que no afectan al programa
    cliente.interpretar_comando('asdasd')
    cliente.interpretar_comando('       ')
    cliente.interpretar_comando('CLASS A : ')
    cliente.interpretar_comando('CLASS : ')
    cliente.interpretar_comando('CLASS : B w a')
    cliente.interpretar_comando('DESCRIBIR')
    cliente.interpretar_comando('CLASS')
