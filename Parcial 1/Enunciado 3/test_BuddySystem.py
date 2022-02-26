# importar BuddySystem
import BuddySystem
import pytest
sistemaDeMem = BuddySystem.BuddySystem(55)




# Test de reservar
def test_RESERVAR_0():
    assert sistemaDeMem.reservar('hi', 1) == 'Se ha alojado la memoria en el bloque (0, 0)'

def test_RESERVAR_1():
    assert sistemaDeMem.reservar('hi', 1) == 'El nombre hi ya esta en uso'

def test_RESERVAR_2():
    assert sistemaDeMem.reservar('je', 20) == 'No hay memoria libre suficiente para alojar al bloque'

def test_RESERVAR_3():
    assert sistemaDeMem.reservar('ju', 2) == 'Se ha alojado la memoria en el bloque (2, 3)'
    
def test_RESERVAR_3():
    assert sistemaDeMem.reservar('big', 16) == 'Se ha alojado la memoria en el bloque (16, 31)'

# Test de liberar

def test_LIBERAR_0():
    assert sistemaDeMem.liberar('no_existo') == 'No hay un bloque con memoria alojada de nombre: no_existo'

def test_LIBERAR_1():
    assert sistemaDeMem.liberar('big') == 'Se ha liberado de memoria el bloque: big (16, 31)'

def test_LIBERAR_2():
    assert sistemaDeMem.liberar('hi') == 'Se ha liberado de memoria el bloque: hi (0, 0)'

# Test mostrar
def test_MOSTRAR():
    assert sistemaDeMem.mostrar()

