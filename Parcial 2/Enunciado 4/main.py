""" Autor: Jesus Bandez. 17-10046
Estudio de la funcion F implementada de tres formas distintas.
Primero se consiguen los valores de alfa y beta
X = 0
Y = 4
Z = 6

alfa = ((0 + 4) mod 5) + 3 = 7
beta = ((4 + 6) mod 5) + 3 = 3
 
"""
from functools import partial
from time import time
from lib.function_F import f

from lib.function_F_tail_recursion import f as recursive_f

from lib.function_F_iterative import f as iterative_f

def measure_time(f, test_number:int):
    """Usada para calcular el tiempo que dura ejecutandose la funcion f

       Retorna: Una tupla donde el primer elemento es lo que retorna la 
        funcion medida y el segundo el tiempo que tado en ejecutarse
    """
    initial_time = time()
    res = f(test_number)
    final_time = time()
    total = final_time - initial_time
    return (res, total)

# funciones evaluadas de manera parcial usadas para probar los casos
# sobre las distintas versiones de f
test_normal_f = partial(measure_time, f)
test_tail_recursion_f = partial(measure_time, recursive_f)
test_iterative_f = partial(measure_time, iterative_f)

# Casos prueba y listas para guardarlos
test_cases = [i for i in range(1, 100)]
test_sol_normal_f = []
test_sol_tail_recursion_f = []
test_sol_iterative_f = []

# Se ejecutan las pruebas 
for test_case in test_cases:
    print('fnormal:')
    test_sol_normal_f.append(test_normal_f(test_case))
    print(test_sol_normal_f[-1])

    print('tail_recursion:')
    test_sol_tail_recursion_f.append(test_tail_recursion_f(test_case))
    print(test_sol_tail_recursion_f[-1])

    print('f_iterative:')
    test_sol_iterative_f.append(test_iterative_f(test_case))
    print(test_sol_iterative_f[-1])

print('Final:')
print('fnormal:')
print(test_sol_normal_f)

print('tail_recursion:')
print(test_sol_tail_recursion_f)

print('f_iterative:')
print(test_sol_iterative_f)


