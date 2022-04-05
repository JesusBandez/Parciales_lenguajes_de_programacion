"""Autor: Jesus Bandez 17-10046
Modulo con la gramatica usada para las expresiones prefijas"""


from . import AST
from .tokenrules import tokens
# -------- REGLAS DE PRECEDENCIA --------
precedence = (
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult', 'TkDiv'),
)


# ---- Producciones -------------
def p_operadores_binarias(p):
    '''expresion : expresion expresion TkPlus 
        | expresion expresion TkMinus 
        | expresion  expresion TkMult 
        | expresion expresion TkDiv 
    '''    
    p[0] = AST.BinOp(p[3], p[1], p[2])

def p_terminal(p):
    'expresion : TkNumber'
    p[0] = AST.Number(int(p[1]))

def p_error(p):
    pass