from . import AST
from .tokenrules import tokens
# -------- REGLAS DE PRECEDENCIA --------
precedence = (
    ('left', 'TkPlus', 'TkMinus'),
    ('left', 'TkMult', 'TkDiv'),
)


# ---- Producciones -------------
def p_operadores_binarias(p):
    '''expresion : TkPlus expresion expresion
        | TkMinus expresion expresion
        | TkMult expresion  expresion
        | TkDiv expresion expresion
    '''    
    p[0] = AST.BinOp(p[1], p[2], p[3])

def p_terminal(p):
    'expresion : TkNumber'
    p[0] = AST.Number(int(p[1]))


def p_error(p):
    pass