
import re

from ply.lex import LexToken

# Definicion de los tokens
tokens = [   
    'TkMult', 'TkDiv', 'TkPlus', 'TkMinus', 'TkNumber'
]

# Se debe ignorar todo tipo de espacio en blanco
t_ignore = ' \t'

# Regex para obtener cada token de operadores
t_TkMult = r'\*'
t_TkDiv = r'/'
t_TkPlus = r'\+'
t_TkMinus = r'-'
t_TkNumber = r'[+-]?\d+'

# Maneja caracteres ilegales
def t_error(t: LexToken):
    t.type = 'IllegalCharacter'
    t.value = t.value[0]

    # Salta el caracter ilegal
    t.lexer.skip(1)
    return t
