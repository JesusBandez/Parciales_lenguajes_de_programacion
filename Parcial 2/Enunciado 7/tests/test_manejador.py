"""Modulo de pruebas para la precedencia de los operadores de las reglas definidas en grammar.py"""
import os
import sys

sys.path.insert(1, os.path.abspath('.'))

import Client
cliente = Client.Client()

def test_manejador(capsys):
    # Diccionarios que simulan los apuntadores
    apuntadores_simulados = {}
    lapidas_simuladas = {}

    # Reservar valor para x
    cliente.interpretar_comando('RESERVAR x valorX')
    apuntadores_simulados['x'] = 0
    lapidas_simuladas [0] = 'valorX'
    assert cliente.VM.apuntadores == apuntadores_simulados
    assert cliente.VM.lapidas == lapidas_simuladas

    # Imprimirlo
    capsys.readouterr()
    cliente.interpretar_comando('IMPRIMIR x')
    captured1 = capsys.readouterr()

    print('valorX')
    captured2 = capsys.readouterr()
    assert captured1 == captured2

    # Reservar valor para y
    cliente.interpretar_comando('RESERVAR y valorY')
    apuntadores_simulados['y'] = 1
    lapidas_simuladas [1] = 'valorY'
    assert cliente.VM.apuntadores == apuntadores_simulados
    assert cliente.VM.lapidas == lapidas_simuladas

    # Reasignar valor para x
    cliente.interpretar_comando('ASIGNAR x y')
    apuntadores_simulados['x'] = 1
    assert cliente.VM.apuntadores == apuntadores_simulados
    assert cliente.VM.lapidas == lapidas_simuladas

    # Imprimir valor de y
    capsys.readouterr()
    cliente.interpretar_comando('IMPRIMIR y')
    captured1 = capsys.readouterr()
    print('valorY')
    captured2 = capsys.readouterr()
    assert captured1 == captured2

    # Liberar valor de y
    cliente.interpretar_comando('LIBERAR y')
    lapidas_simuladas[1] = None
    assert cliente.VM.apuntadores == apuntadores_simulados
    assert cliente.VM.lapidas == lapidas_simuladas

    capsys.readouterr()
    cliente.interpretar_comando('IMPRIMIR x')
    captured1 = capsys.readouterr()

    print('ERROR, el nombre "x" no apunta a un valor válido')
    captured2 = capsys.readouterr()
    assert captured1 == captured2

    # Apuntadores inexistentes
    capsys.readouterr()
    cliente.interpretar_comando('ASIGNAR j k')
    captured1 = capsys.readouterr()
    print(f'No existe el apuntador "j"')
    captured2 = capsys.readouterr()
    assert captured1 == captured2

    cliente.interpretar_comando('ASIGNAR x k')
    captured1 = capsys.readouterr()
    print(f'No existe el apuntador "k"')
    captured2 = capsys.readouterr()
    assert captured1 == captured2

    # Ejecucion de comandos que no deben arrojar excepciones
    cliente.interpretar_comando('asfdaf')
    cliente.interpretar_comando('RESERVAR ')
    cliente.interpretar_comando('ASIGNAR ')
    cliente.interpretar_comando('IMPRIMIR ')
    cliente.interpretar_comando('LIBERAR ')



