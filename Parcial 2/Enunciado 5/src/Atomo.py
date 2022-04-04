from dataclasses import dataclass
from src.Tipo import *


@dataclass
class Atomo(Tipo):
   nombre:str
   representacion:int
   alineacion:int
