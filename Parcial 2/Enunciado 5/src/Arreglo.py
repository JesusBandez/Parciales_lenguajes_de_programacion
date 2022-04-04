from dataclasses import dataclass
from src.Tipo import *

@dataclass
class Arreglo(Tipo):
    nombre:str
    tipo:str
    tamanio:int