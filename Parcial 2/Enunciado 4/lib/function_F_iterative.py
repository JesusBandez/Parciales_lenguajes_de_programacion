"""Autor: Jesus Bandez. 17-10046
Conversion a iterativa de la funcion f dada en el enunciado"""

def f(n:int) -> int:
    # Se inicializan los valores de c y de la lista x.
    # Esto corresponde a la llamada inicial de la funcion f_aux en
    # la version iterativa de cola
    c = 20
    x = [i for i in range(0, 22)]


    # Componente del caso base cuando  0 <= n < 21
    if 0 <= n < 21:
        return n

    # Componente del caso recursivo:
    # Mientras n no sea c + 1
    while n != c+1:    
        # Se obtiene el valor de la f evaluada en c y se guarda en
        # la ultima posicion de la lista x
        x[21] = sum_list(x)
        for i in range(1, 22):
            x[i-1] = x[i]

        c += 1

    # Cuando c+1 == n, se tiene que f(c+1) = f(n). Por tanto, se
    # hace el ultimo calculo y se retorna el valor buscado
    return sum_list(x)

def sum_list(x):
    """Funcion auxiliar usada para calcular la suma de una lista"""
    return sum([x[21 - i*3] for i in range(1, 8)])