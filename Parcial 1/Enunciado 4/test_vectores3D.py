import Vectores3D
import pytest
import math

# Se inicializan los vectores. Las pruebas se hacen con estos valores concretos
vecA = Vectores3D.Vector3D(1, 2, 3)
vecB = Vectores3D.Vector3D(2, -1, -2)
vecC = Vectores3D.Vector3D(3, 1, 2)

vecAfloat = Vectores3D.Vector3D(1.1, 2.2, 3.1)
vecBfloat = Vectores3D.Vector3D(0.1, 0.2, 0.1)

# Test de equivalencia con error de tipo
def test_eq_vectores0():
    with pytest.raises(TypeError):
        assert vecA == ''

# Test de sumas con vector, float y strings
def test_suma_vectores0():
    assert vecA + vecB == Vectores3D.Vector3D(3, 1, 1)

def test_suma_vectores1():
    assert vecAfloat + vecBfloat == Vectores3D.Vector3D(1.2, 2.4, 3.2)

def test_suma_vectores2():
    assert vecAfloat + 1.1 ==  Vectores3D.Vector3D(2.2, 3.3, 4.2)

def test_suma_vectores3():
    with pytest.raises(TypeError):
        assert vecA + ''

# Test de restas y negacion de un vector
def test_resta_vectores0():
    assert vecA - vecB == Vectores3D.Vector3D(-1, 3, 5)

def test_resta_vectores1():
    assert vecAfloat - vecBfloat == Vectores3D.Vector3D(1.0, 2.0, 3.0)

def test_resta_vectores2():
    assert vecAfloat - 1.1 == Vectores3D.Vector3D(0.0, 1.1, 2.0)

def test_resta_vectores3():
    with pytest.raises(TypeError):
        assert vecA - ''

def test_neg_vectores():
    assert - vecB == Vectores3D.Vector3D(-2, 1, 2)

# test de conversion a string
def test_str_vectores():
    assert str(vecA) == '(1, 2, 3)'

# test de producto vectorial, y producto con entero y flotante
def test_mul_vectores0():
    assert vecA * vecB == Vectores3D.Vector3D(-1, 8, -5)

def test_mul_vectores1():
    assert vecAfloat * vecBfloat == Vectores3D.Vector3D(-0.4, 0.2, 0)

def test_mul_vectores2():
    assert vecA * 2 == Vectores3D.Vector3D(2, 4, 6)

def test_mul_vectores3():
    assert vecA * 3.2 == Vectores3D.Vector3D(3.2, 6.4, 9.6)

def test_mul_vectores4():
    with pytest.raises(TypeError):
        assert vecA * ''

# test de producto punto

def test_mod_vectores0():
    assert vecA%vecB == -6

def test_mod_vectores1():
    assert math.isclose(vecAfloat%vecBfloat, 0.86)

def test_mod_vectores0():
    with pytest.raises(TypeError):
        assert vecA%'' 

# test con algunas operaciones
def test_operacion_vectores0():
    assert vecA * vecB + vecC == Vectores3D.Vector3D(2, 9, -3)

def test_operacion_vectores1():
    assert vecA % (vecC * vecB) == 5