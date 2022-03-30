import os
import sys
import pytest


p = os.path.abspath('.')
sys.path.insert(1, p)

from src.VM import VM as VM
import ply.lex as lex


vm = VM()

test_cases = [
    ('+ 2 2', '2 2 +')
]
test_sol = [
    '2 + 2'
]

test_cases.append(('+ + 2 3 1',' 2 3 1 + +' ))
test_sol.append('2 + 3 + 1')

test_cases.append(('+ - 2 3 1',' 2 3 - 1 +' ))
test_sol.append('2 - 3 + 1')

test_cases.append(('- 30 * 10 + 4 3',' 30 10 4 3 + * -' ))
test_sol.append('30 - 10 * (4 + 3)')

cases = list(zip(test_cases, test_sol))
@pytest.mark.parametrize("test_case,test_sol", cases)
def test_failed(test_case:str, test_sol:object, capsys):   
    
    # Mostrar el resultado del ast por salida estandar
    print(vm.mostrar('PRE', test_case[0]))
    captured1 = capsys.readouterr()

    print(vm.mostrar('POST', test_case[1]))
    captured2 = capsys.readouterr()

    # Simular la salida esperada del caso prueba y capturarla
    print(test_sol)
    captured3 = capsys.readouterr()

    # Comprobar las salidas
    assert captured1.out == captured2.out
    assert captured1.out == captured3.out