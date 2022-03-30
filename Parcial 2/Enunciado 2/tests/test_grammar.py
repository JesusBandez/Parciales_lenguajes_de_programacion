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
test_cases.append('+ 2 2 ')
test_sol.append(BinOp('+', Number(2), Number(2)))

test_cases.append('* 3 9 ')
test_sol.append(BinOp('*', Number(3), Number(9)))

test_cases.append('/ 3 9 ')
test_sol.append(BinOp('/', Number(3), Number(9)))

test_cases.append('- 3 9 ')
test_sol.append(BinOp('-', Number(3), Number(9)))

test_cases.append('+ - 3 9 1')
test_sol.append(BinOp('+', BinOp('-', Number(3), Number(9)), Number(1)))

test_cases.append('+ - + 3 9 1 2')
test_sol.append(BinOp('+', BinOp('-',BinOp('+',  Number(3),  Number(9)), Number(1)), Number(2)))

test_cases.append('+ * + 3 9 1 2')
test_sol.append(BinOp('+', BinOp('*',BinOp('+',  Number(3),  Number(9)), Number(1)), Number(2)))

test_cases.append('/ * + 3 9 1 2')
test_sol.append(BinOp('/', BinOp('*',BinOp('+',  Number(3),  Number(9)), Number(1)), Number(2)))

test_cases.append('/ * + 3 9 1 + 1 2')
test_sol.append(BinOp('/', BinOp('*',BinOp('+',  Number(3),  Number(9)), Number(1)), BinOp('+', Number(1), Number(2))))

cases = list(zip(test_cases, test_sol))
@pytest.mark.parametrize("test_case,test_sol", cases)
def test_prefix_grammar_rules(test_case:str, test_sol:object):
    ast = vm.test_parser("PRE", test_case)
    assert ast == test_sol



# Prueba para la gramatica Postfija
test_cases, test_sol = [], []
test_cases.append('2 2 +' )
test_sol.append(BinOp('+', Number(2), Number(2)))

test_cases.append('3 9 *')
test_sol.append(BinOp('*', Number(3), Number(9)))

test_cases.append('3 9 /')
test_sol.append(BinOp('/', Number(3), Number(9)))

test_cases.append('3 9 -')
test_sol.append(BinOp('-', Number(3), Number(9)))

test_cases.append('1 9 3 - +')
test_sol.append(BinOp('+',  Number(1) , BinOp('-', Number(9), Number(3))))

test_cases.append('3 9 1 2 + - +')
test_sol.append(BinOp('+', Number(3), BinOp('-', Number(9) ,BinOp('+',  Number(1),  Number(2)))))

test_cases.append('3 9 1 2 + * +')
test_sol.append(BinOp('+',  Number(3), BinOp('*', Number(9), BinOp('+',  Number(1),  Number(2)))))

test_cases.append('2 1 + 9 1 2 / * +')
test_sol.append(BinOp('+', BinOp('+', Number(2), Number(1)), BinOp('*', Number(9), BinOp('/',  Number(1),  Number(2)))))



cases = list(zip(test_cases, test_sol))
@pytest.mark.parametrize("test_case,test_sol", cases)
def test_postfix_grammar_rules(test_case:str, test_sol:object):
    ast = vm.test_parser("POST", test_case)
    assert ast == test_sol
