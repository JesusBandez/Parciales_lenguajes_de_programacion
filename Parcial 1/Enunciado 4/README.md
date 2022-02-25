# Codigos del enunciado 4
## Instrucciones y ejemplos
En este directorio están los códigos que corresponden a 
 la implementación de un módulo que define el tipo de vectores de 3 dimensiones.

La implementación está hecha en python. Para usarla, necesita descargar python
de su [página web](https://www.python.org/downloads/)



Los vectores están implementados como una clase llamada `Vector3D`. 
Esta clase se encuentra en el módulo `Vectores3D`.

Para empezar a usar los vectores, primero debe descargar el módulo
`Vectores3D` y colocarlo en el directorio donde se encuentre su programa.

Luego, debe importar el módulo con `import Vectores3D` e instanciar la clase `Vector3D`

Vectores3D permite distintas operaciones con vectores de 3 dimensiones usando los
operadores '+' '-' '*' '%'. Por ejemplo: basta con tener dos instancias de la clase y usar el
el operador '+' para obtener la suma de dos vectores. El siguiente código sirve como ejemplo:

```
import Vectores3D

vecA = Vectores3D.Vector3D(1,-1,1)
vecB = Vectores3D.Vector3D(2,2,1)
vecC = Vectores3D.Vector3D(0,0,-1)

print(vecA + vecB)
# Se obtiene Vector3D con coordenadas (3,1,2)

print(vecA - vecB)
# Se obtiene Vector3D con coordenadas (-1,-3,0)

print(vecA * vecB)
# Se obtiene Vector3D con coordenadas (-3,1,4)

print(vecA * 3)
# Se obtiene Vector3D con coordenadas (3,-3,3)

print(vecB + 2)
# Se obtiene Vector3D con coordenadas (4,4,3)

print(vecB == vecC + 2)
# Se obtiene True 
```

## Ejecutando la testunit
En el directorio `Resultados Units tests`, en el archivo `index.html` se encuentran 
los resultados de las pruebas ejecutadas. Sin embargo, puede ejecutar las pruebas descargando `pytest`
con el comando:
`pip install pytest`

Luego, necesita instalar `coverage` para ello también se usa pip: `pip install coverage`

Con las dependencias ya instaladas, basta con ejecutar los siguientes comandos:
```
coverage run -m pytest
coverage report
```

Obtendrá en pantalla los resultados de las pruebas que se encuentran en el archivo `test_vectores3D.py` estas pruebas
consiguen una cobertura del 100% sobre el código del módulo `Vectores3D`