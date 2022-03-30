import os
import sys
import pytest


p = os.path.abspath('.')
sys.path.insert(1, p)

from src.VM import VM as VM
import ply.lex as lex

def simulate_token(type, value=None):
    val = ''
    if type == 'TkId':
        val = f'("{value}")'
    elif type == 'TkNumber':
        val = f'({value})'

    return f'{type}{val}'

def custom_repr(t: lex.LexToken):
    val = ''
    if t.type == 'TkId':
        val = f'("{t.value}")'
    elif t.type == 'TkNumber':
        val = f'({t.value})'

    return f'{t.type}{val}'

lex.LexToken.__repr__ = custom_repr

vm = VM()

test_cases = [
    "2"
]
test_sol = [
    [simulate_token('TkNumber', 2)]
]

test_cases.append('2 + 2')
test_sol.append([simulate_token('TkNumber', 2), simulate_token('TkPlus'), simulate_token('TkNumber', 2)])

test_cases.append('2 * 2')
test_sol.append([simulate_token('TkNumber', 2), simulate_token('TkMult'), simulate_token('TkNumber', 2)])

test_cases.append('2 / 2')
test_sol.append([simulate_token('TkNumber', 2), simulate_token('TkDiv'), simulate_token('TkNumber', 2)])

test_cases.append('2 - 2')
test_sol.append([simulate_token('TkNumber', 2), simulate_token('TkMinus'), simulate_token('TkNumber', 2)])

test_cases.append('@')
test_sol.append(['IllegalCharacter'])


cases = list(zip(test_cases, test_sol))
@pytest.mark.parametrize("test_case,test_sol", cases)
def test_lexer(test_case:str, test_sol:object, capsys):
    tokens = vm.test_tokenizer(test_case)
    tokens_str = list(map(lambda x: x.__str__(), tokens))
    
    # Mostrar los tokens por salida estandar
    print(tokens_str)
    captured1 = capsys.readouterr()

    # Simular la salida esperada del caso prueba y capturarla
    print(test_sol)
    captured2 = capsys.readouterr()

    # Comprobar las salidas
    assert captured1.out == captured2.out