""" Autor: Jesus Bandez. 17-10046
  Modulo con la version recursiva de cola  de la formula de la funcion f.
    
   
   La estrategia de esta version consiste en "voltear" la forma en que se
   calculan los valores de la funcion. En vez de empezar en el valor 'n' y
   'bajar' para calcularlo segun los valores bases, se inicia en los 
   valores bases y se va 'subiendo' calculando los siguientes n+1 con los 
   casos bases.
   """


# Funcion f iterativa de cola
def f(n:int) -> int:
    'Version recursiva de cola de la funcion f'

    # Retorna el valor de la funcion auxiliar.
    return f_aux(n, [i for i in range(0, 22)], 20)


def f_aux(n:int, x:list, c:int) -> int:
    """Funcion recursiva auxiliar para calcular los valores de f. Es necesario
    inicializar el valor x con los valores bases donde x[i] es el valor f(n) con
    0 <= n < 21. y el valor c se inicializa en 20
    
    Para calcular f(n) se procede a calcular f(20), se guarda el valor en la ultima
    posicion de la lista x, y luego se hace una llamada recursiva para calcular 
    el valor de f(21). Los valores necesarios para obtener el valor de funcion f(c)
    se mantienen en la lista x. Cuando n == c+1, se consigue el valor f(n)
    """

    # Caso base de la recursion
    if 0 <= n < 21:
        return x[n]

    # Si se ha alcanzado el valor n buscado, entonces se calcula f(n) y se retorna
    elif n == c+1:
        return sum_list(x)
    
    # Si no, entonces es necesario calcular el valor f(c) y hacer la llamada recursiva
    else:
        # Se obtiene la suma de los valores ya calculados y se asigna como el ultimo
        # valor de la lista
        x[21] = sum_list(x)

        # Se mueven hacia atras los valores calculados
        for i in range(1, 22):
            x[i-1] = x[i]
        
        # Se calcula el siguiente valor. Fijese que esta es la unica llamda recursiva
        # en toda la funcion. Como es lo ultimo en ejecutarse en cada llamada recursiva,
        # es facil ver que esta version de la funcion f es de cola.
        return f_aux(n, x, c+1)

def sum_list(x):
    """Funcion auxiliar usada para calcular la suma de una lista"""
    return sum([x[21 - i*3] for i in range(1, 8)])

