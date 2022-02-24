""" Autor: Jesus Bandez 1710046
Una libreria con implementacion de la clase de un vector de 3 dimensiones.
Se sobrecargan los operadores "+ - * %" para que correspondan con la suma de 
vectores, la resta, el producto vectorial y el producto punto.
"""

# Libreria usada para comparar de manera correcta los floats
import math


class Vector3D(object):
    """Clase vector de 3 dimensiones.
    Esta clase permite la manipulacion de vectores de 3 dimensiones.
        
        Se inicializa con:
            a: Primera coordenada del vector
            b: Segunda coordenada del vector
            c: Tercera coordenada del vector"""
  
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        "La representacion del vector en string es una tupla de la forma (a,b,c)"
        return str((self.a, self.b, self.c))

    def __eq__(self, otroOperando):
        """Operador == sobrecargado para permitir comparar dos objetos Vector3D.
        Dos vectores son iguales si todas sus componentes de la misma posicion son iguales """
        # Se comprueba que el otro operando sea un Vector3D. De no serlo, se arroja
        # un error de tipo

        if isinstance(otroOperando, Vector3D):
            # Es necesario usar la funcion de isclose de math por la imprecision de los floats
            return ( math.isclose(self.a, otroOperando.a) and
                math.isclose(self.b, otroOperando.b) and
                math.isclose(self.c, otroOperando.c))
        else:
            raise TypeError("Unsupported operand type(s) for ==: 'Vector3D' and '{}'".format(
                type(otroOperando)
                ))

    def __neg__(self):
        """Operador - unario sobrecargado. 
            Se invierte las componentes del vector

            Retorna un vector3D de la forma: (-a, -b, -c)
        """   
        return Vector3D(
            -self.a ,
            -self.b ,
            -self.c )

    def __add__(self, otroOperando):
        """Operador + sobrecargado. 
        Se suman las componentes del vector con otro vector3D O con un numero entero o float.

            Retorna un vector3D de la forma: 
                (a0+1, b0+b1, c0+c1) si es una suma de vectores3D 
                (a0+n, b0+n, c0+n) si es una suma con un numero n
        """
        # Comprobar si el otro operando es un vector y retornar un vector3D con la suma de sus
        # componentes 
        if isinstance(otroOperando, Vector3D):
            return Vector3D(
                self.a + otroOperando.a,
                self.b + otroOperando.b,
                self.c + otroOperando.c)
        
        # Si el otro operando es un numero, se suman las componentes del vector con el
        # numero y se retornan en un vector
        elif isinstance(otroOperando, int) or isinstance(otroOperando, float):
            return Vector3D(
                self.a + otroOperando,
                self.b + otroOperando,
                self.c + otroOperando
                )

        # No se soporta la suma con otro tipo de datos
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector3D' and '{}'".format(
                type(otroOperando)))

    def __sub__(self,otroOperando):
        """Operador - sobrecargado. 
        Se restan las componentes del vector con otro vector3D O con un numero entero o float.

            Retorna un vector3D de la forma: 
                (a0-1, b0-b1, c0-c1) si es una resta de vectores3D 
                (a0-n, b0-n, c0-n) si es una resta con un numero n
        """

        # Comprobar si el otro operando es un vector y retornar un vector3D con la resta de sus
        # componentes 
        if isinstance(otroOperando, Vector3D):
            return Vector3D(
                self.a - otroOperando.a,
                self.b - otroOperando.b,
                self.c - otroOperando.c
                )

        # Si el otro operando es un numero, se restan las componentes del vector con el
        # numero y se retornan en un vector
        elif isinstance(otroOperando, int) or isinstance(otroOperando, float):
            return Vector3D(
                self.a - otroOperando,
                self.b - otroOperando,
                self.c - otroOperando
                )

        # No se soporta la resta con otro tipo de datos
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Vector3D' and '{}'".format(
                type(otroOperando)
                ))



    def __mul__(self, otroOperando):
        """ Sobrecarga de * sobrecargado
            Se consigue el producto vectorial de dos vectores o se multiplica cada componente del 
                vector por un numero

            Retorna: 
            Un vector3D de la forma: ( b0*c1 - c0*b1, c0*a1 - a0*c1, a0*b1 - b0*a1) si es producto vectorial
            Un vector3D de la forma: (a*n, b*n, c*n) si producto con un numero n
            
            """

        # Comprobar si el otro operando es un vector y retornar un vector3D con el producto vectorial
        # entre ellos
        if isinstance(otroOperando, Vector3D):
            return Vector3D(
                self.b*otroOperando.c - self.c*otroOperando.b,
                self.c*otroOperando.a - self.a*otroOperando.c,
                self.a*otroOperando.b - self.b*otroOperando.a
                )

        # Comprobar si el otro operando es un numero y retornar un vector3D con cada componente
        # multiplicada por el numero
        elif isinstance(otroOperando, int) or isinstance(otroOperando, float):
            return Vector3D(
                self.a * otroOperando,
                self.b * otroOperando,
                self.c * otroOperando
                )

        # En cualquier otro caso, se arroja un error de tipo
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector3D' and '{}'".format(
                type(otroOperando)
                ))

    def __mod__(self, otroOperando):
        """Operador % sobrecargado.
            Se consigue el producto punto de dos vectores.
            Retorna un numero siendo el producto punto entre los vectores
        """

        # Comprobar si el otro operando es un vector y retornar un vector3D con el producto punto
        # entre ellos
        if isinstance(otroOperando, Vector3D):
            return (self.a*otroOperando.a +
                    self.b*otroOperando.b +
                    self.c*otroOperando.c
                    )
        # En cualquier otro caso, se arroja un error de tipo
        else:
            raise TypeError("Unsupported operand type(s) for %: 'Vector3D' and '{}'".format(
                type(otroOperando)
                ))
            