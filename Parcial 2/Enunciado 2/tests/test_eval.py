import os
import sys
import pytest


p = os.path.abspath('.')
sys.path.insert(1, p)

from src.VM import VM as VM
import ply.lex as lex
import ply.yacc as yacc
from src.AST import *
from src.VM import VM 


# Prueba para la gramatica prefija
vm = VM()

test_cases, test_sol = [], []

test_cases.append( ('+ 2 2', '2 2 +') )
test_sol.append(4)

test_cases.append( ('* 2 3', '2 3 *') )
test_sol.append(6)

test_cases.append( ('/ 10 4', '10 4 /') )
test_sol.append(2)

test_cases.append( ('- / 10 4 1', '10 4 / 1 -') )
test_sol.append(1)

test_cases.append( ('* - / 10 4 1 30', '10 4 / 1 - 30 *') )
test_sol.append(30)

cases = list(zip(test_cases, test_sol))
@pytest.mark.parametrize("test_case,test_sol", cases)
def test_eval(test_case:str, test_sol:object):
    prefix_eval = vm.test_parser("PRE", test_case[0]).eval()
    postfix_eval = vm.test_parser("POST", test_case[1]).eval()
    assert prefix_eval == test_sol
    assert prefix_eval == postfix_eval
