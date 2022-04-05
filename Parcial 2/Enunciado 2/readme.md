# Codigos del Enunciado 2

Codigos del programa que maneja las expresiones aritmeticas de enteros
tanto de reden pre-fijo como en orden post-fijo.

Este manejador recibe expresiones y su orden, y es capaz de traducirlas a 
expresiones en orden infijo o evaluarlas

Para ejecutar el programa, necesita descargar Python
de su [página web](https://www.python.org/downloads/)

Se incluyen tanto los archivos de las pruebas unitarias como la clase que maneja al sistema y un cliente para esta clase.

Para poder iniciar el cliente, debe ejecutar el siguiente comando en el directorio:

```
.> python Client.py
```

Una vez ejecutado el programa, puede interactuar con él usando los comandos
que él le describe, siendo estos los mismos que se pueden leer en el enunciado

## Ejecutando la testunit
En el directorio `Resultados Units tests`, en el archivo `index.html` se encuentran 
los resultados de las pruebas ejecutadas. Puede abrir este archivo con su navegador para 
ver el reporte de cobertura. 

Tambien, puede ejecutar las pruebas descargando `pytest`
con el comando:
`pip install pytest`

Luego, necesita instalar `coverage`. Para ello, también se usa pip: `pip install coverage`

Con las dependencias ya instaladas, basta con ejecutar los siguientes comandos:
```
coverage run -m pytest
coverage report
```

Obtendrá en pantalla los resultados de las pruebas que se encuentran en el archivo `test_manejador.py` estas pruebas
consiguen una cobertura del 84% sobre todo el código, excepto para las clases de la librería PLY.