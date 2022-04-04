from dataclasses import dataclass
from src.Tipo import *

@dataclass
class Struct(Tipo):
    nombre:str
    tipos:list