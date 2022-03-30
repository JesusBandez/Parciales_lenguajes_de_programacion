"""Modulo con las clases que construyen el arbol sintactico"""
import operator
# Diccionario de las operaciones
OPERATORS = {
    '*' : operator.mul,
    '+' : operator.add,
    '-' : operator.sub,
    '/' : operator.floordiv
}


class AST:
    def __repr__(self) -> str:
        return self.__str__()


class BinOp(AST):
    def __init__(self, op: str, lhs_term: object, rhs_term: object):
        self.op = op
        self.lhs_term = lhs_term
        self.rhs_term = rhs_term

    def __str__(self) -> str:
        res = ''
        if self.comprobar_precedencia(self.lhs_term):
            res += f'({self.lhs_term}) {self.op}'
        else:
            res += f'{self.lhs_term} {self.op}'

        if self.comprobar_precedencia(self.rhs_term):
            res += f' ({self.rhs_term})'
        else:
            res += f' {self.rhs_term}'
            
        return res
        
        

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (self.op == other.op 
                and self.lhs_term == other.lhs_term 
                and self.rhs_term == other.rhs_term)
        else:
            raise TypeError(f'{type(self).__name__} is not {type(other).__name__}')

    def eval(self):
        return OPERATORS[self.op](self.lhs_term.eval(), self.rhs_term.eval())
    
    def comprobar_precedencia(self, term: AST):
        
        return isinstance(term, BinOp) and self.op in ['*', '/'] and term.op in ['+', '-']



class Number(AST):
    def __init__(self, value: object):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> str:
        if isinstance(other, type(self)):
            return self.value == other.value
        else:
            raise TypeError(f'{type(self).__name__} is not {type(other).__name__}')

    def eval(self):
        return self.value