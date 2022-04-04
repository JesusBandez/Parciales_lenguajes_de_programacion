"""Modulo de pruebas para la precedencia de los operadores de las reglas definidas en grammar.py"""
import os
import sys

sys.path.insert(1, os.path.abspath('.'))

import Client
from src.Atomo import *
from src.Arreglo import *
from src.Struct import * 
from src.msg_describir import *

cliente = Client.Client()

def test_manejador(capsys):
    # Diccionarios que simulan los tipos
    atomos_simulados = {}
    arreglos_simulados = {}
    registros_simulados = {}

    # Agregar atomo
    cliente.interpretar_comando('ATOMICO bool 1 2')
    atomos_simulados['bool'] = Atomo('bool', 1, 2)

    assert cliente.VM.atomos == atomos_simulados

    # Agregar otro atomo
    cliente.interpretar_comando('ATOMICO int 4 4')
    atomos_simulados['int'] = Atomo('int', 4, 4)
    assert cliente.VM.atomos == atomos_simulados

    # Agregar atomo de mismo nombre, no deben haber cambios
    cliente.interpretar_comando('ATOMICO int 20 100')
    # Comandos sin sentido para probar que no hayan cambios
    cliente.interpretar_comando('ATOMICO x  100')
    cliente.interpretar_comando('ATOMICO x rata 100')
    cliente.interpretar_comando('4T0M1C0 x 20 100')
    assert cliente.VM.atomos == atomos_simulados

    # Agregar un arreglo de tres enteros
    cliente.interpretar_comando('ARREGLO enterosArray int 3')
    arreglos_simulados['enterosArray'] = Arreglo('enterosArray', 'int', 3)
    assert (cliente.VM.atomos == atomos_simulados 
        and cliente.VM.arreglos == arreglos_simulados)

    # Agregar arreglo de dos booleanos
    cliente.interpretar_comando('ARREGLO booleanosArray bool 2')
    arreglos_simulados['booleanosArray'] = Arreglo('booleanosArray', 'bool', 2)
    assert (cliente.VM.atomos == atomos_simulados 
        and cliente.VM.arreglos == arreglos_simulados)

    # Comandos sin sentido o malos que no deben alterar los diccionarios de la VM
    cliente.interpretar_comando('ARREGLO pocos_argumentos 2')
    cliente.interpretar_comando('ARREGLO booleanos muchos_argumentos demasiados ')
    cliente.interpretar_comando('ARREGLO booleanos noExisto 2')    
    cliente.interpretar_comando('ARREGLO enterosArray bool 2') # nombre de arreglo existente
    cliente.interpretar_comando('ARREGL comando_mal_escrito bool 2')
    cliente.interpretar_comando('ARREGLO int int 2') # nombre de atomo ya definido
    assert (cliente.VM.atomos == atomos_simulados 
        and cliente.VM.arreglos == arreglos_simulados)

    # Crear registros
    cliente.interpretar_comando('STRUCT dosBoolConArreglo [bool bool booleanosArray]')
    registros_simulados['dosBoolConArreglo'] = Struct('dosBoolConArreglo', 
        ['bool', 'bool', 'booleanosArray'])

    assert (cliente.VM.atomos == atomos_simulados and cliente.VM.arreglos == arreglos_simulados
        and cliente.VM.registros == registros_simulados)

    cliente.interpretar_comando('STRUCT enterosYBools [enterosArray booleanosArray enterosArray]')
    registros_simulados['enterosYBools'] = Struct('enterosYBools', 
        ['enterosArray', 'booleanosArray', 'enterosArray'])

    assert (cliente.VM.atomos == atomos_simulados and cliente.VM.arreglos == arreglos_simulados
        and cliente.VM.registros == registros_simulados)

    # Comandos sin sentido que no deben cancelar la ejecucion del programa ni modificar el estado
    # de la VM
    cliente.interpretar_comando('STRUCT enterosYBools [booleanosArray]')
    cliente.interpretar_comando('STRUCT listaVacia []')
    cliente.interpretar_comando('STRUCT noExisteEquisDe [esVerdadQuenoExistoEquisDe]')
    cliente.interpretar_comando('')
    cliente.interpretar_comando('ATOMICO hola!ra 2 2')
    cliente.interpretar_comando('ATOMICO hola!raOtraVez [dosBoolConArreglo]')

    assert (cliente.VM.atomos == atomos_simulados and cliente.VM.arreglos == arreglos_simulados
        and cliente.VM.registros == registros_simulados)

    assert (cliente.VM.atomos == atomos_simulados and cliente.VM.arreglos == arreglos_simulados
        and cliente.VM.registros == registros_simulados)
    

    # Borrar la salida actual
    capsys.readouterr()

    # Describir bool
    cliente.interpretar_comando('DESCRIBIR bool')
    capture1 = capsys.readouterr()

    # Simular la salida
    sol = [1, 2, 0]
    describir_empaquetamiento_completo(*sol)
    describir_empaquetamiento_solo_de_registros(*sol)
    describir_sin_empaquetamiento(*sol)
    describir_reordenando_campos(*sol)
    capture2 = capsys.readouterr()
    assert capture1.out == capture2.out

    # Describir booleanosArray
    cliente.interpretar_comando('DESCRIBIR booleanosArray')
    capture1 = capsys.readouterr()

    # Simular la salida
    sol = [2, 2, 0]
    describir_empaquetamiento_completo(*sol)
    describir_empaquetamiento_solo_de_registros(*sol)
    describir_sin_empaquetamiento(*sol)
    describir_reordenando_campos(*sol)
    capture2 = capsys.readouterr()
    assert capture1.out == capture2.out

    # Describir la estructura dosBoolConArreglo
    cliente.interpretar_comando('DESCRIBIR dosBoolConArreglo')
    capture1 = capsys.readouterr()

    # Simular la salida    
    describir_empaquetamiento_completo(4, 2, 0)
    describir_empaquetamiento_solo_de_registros(6, 2, 2)
    describir_sin_empaquetamiento(6, 2, 2)
    describir_reordenando_campos(5, 2, 1)
    capture2 = capsys.readouterr()
    assert capture1.out == capture2.out

    # Crear una nueva estructura y describirla
    cliente.interpretar_comando('STRUCT test [bool booleanosArray bool dosBoolConArreglo]')
    capsys.readouterr()

    cliente.interpretar_comando('DESCRIBIR test')
    capture1 = capsys.readouterr()
    # Simular la salida
    describir_empaquetamiento_completo(8, 2, 0)
    describir_empaquetamiento_solo_de_registros(11, 2, 3)
    describir_sin_empaquetamiento(12, 2, 4)
    describir_reordenando_campos(9, 2, 1)
    capture2 = capsys.readouterr()
    assert capture1.out == capture2.out









