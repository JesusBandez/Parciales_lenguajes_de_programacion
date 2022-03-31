""" Autor: Jesus Bandez. 17-10046
  Modulo con la version recursiva que es una traduccion directa de la formula
   de la funcion"""

def f(n: int) -> int:
    # Si es un caso base, se retorna n
    if 0 <= n < 21:
        return n

    else:
        # La llamada recursiva crea una lista con los valores anteriores
        # y luego los suma
        return sum([f(n - 3* i) for i in range(1, 8)])