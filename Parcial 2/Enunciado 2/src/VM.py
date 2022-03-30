"""Clase que implementa la Virtual Machine encargada de hacer las traducciones 
    y evaluaciones"""
import math
import ply.lex as lex
import src.tokenrules
import src.AST
import ply.yacc as yacc
import src.postfix_grammar
import src.prefix_grammar


class VM(object):
    
    def __init__(self):
        """ Clase que implementa un parser para las traducciones de expresiones
            infijas y posfijas"""

        self.lexer = lex.lex(module=src.tokenrules)
        self.prefix_parser = yacc.yacc(module=src.prefix_grammar)
        self.postfix_parser  = yacc.yacc(module=src.postfix_grammar)

    def eval(self, orden: str, expr:str):
        """ Metodo que recibe un orden y una expresion en ese orden, y retorna 
            la evaluacion de la expresion
            Recibe:
                orden: representa en que orden esta la expresion
                expr: expresion a evaluar
            Retorna:
                res: Resultado de evaluar la expresion
        """
        if orden == "PRE":
            ast = self.prefix_parser.parse(expr, lexer=self.lexer)
        elif orden == "POST":
            ast = self.postfix_parser.parse(expr, lexer=self.lexer)
        
        if ast:
            return f'{ast.eval()}'

        else:
            return f'Hay un error de sintaxis en la expresion: {expr}'

    
    def mostrar(self, orden:str, expr:str):
        """Metodo que muestra en orden infijo la expresion pasada como 
            argumento que está en el orden pasado como argumento
            Recibe:
                orden: Representa en que orden esta la expresion
                expr: Expresion a traducir a infijo
            Retorna:
                res: Resultado traducir la expresion a infijo
        """
        if orden == "PRE":
            ast = self.prefix_parser.parse(expr, lexer=self.lexer)
        elif orden == "POST":
            ast = self.postfix_parser.parse(expr, lexer=self.lexer)
        
        if ast:
            return f'{ast}'

        else:
            return f'Hay un error de sintaxis en la expresion: {expr}'

    def test_tokenizer(self, expr:str) -> list:
        """Recibe una string y retorna una lista de tokens. En caso de
        de algun error en los tokens, arroja una exception"""
        self.lexer.input(expr)

        tokens = []

        for token in self.lexer:         
                tokens.append(token)

        return tokens


    def test_parser(self, orden:str, expr:str) -> object:
        """Recibe una string y retorna un AST con la sintaxis de la string
        Retorna None en caso de error al leer al sintaxis"""
        if orden == "PRE":
            return self.prefix_parser.parse(expr, lexer=self.lexer)
        elif orden == "POST":
            return self.postfix_parser.parse(expr, lexer=self.lexer)
        else:
            return None




