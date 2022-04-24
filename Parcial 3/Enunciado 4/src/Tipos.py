from dataclasses import dataclass


@dataclass
class Tipo(object):
    nombre: str
    super_clase: object
    metodos: list[str]

    def __str__(self) -> str:
        if self.super_clase:
            return f'<{self.nombre}> : <{self.super_clase.nombre}>'
        else:
            return f'<{self.nombre}>'

    def __repr__(self) -> str:
        return self.__str__()