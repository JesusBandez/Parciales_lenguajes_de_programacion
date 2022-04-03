# Codigos del Enunciado 7

Estos codigos corresponden a la implementación del simulador del sistema de manejo de memoria dinámica con liberación explícita en Python.

Para usarla, necesita descargar Python
de su [página web](https://www.python.org/downloads/)

Se incluyen tanto los archivos de las pruebas unitarias como la clase que maneja al sistema y un cliente para esta clase.

Para poder iniciar el cliente, debe ejecutar el siguiente comando en el directorio:

```
.> python Client.py
```


## Ejecutando la testunit
En el directorio `Resultados Units tests`, en el archivo `index.html` se encuentran 
los resultados de las pruebas ejecutadas. Puede ejecutar las pruebas descargando `pytest`
con el comando:
`pip install pytest`

Luego, necesita instalar `coverage` para ello también se usa pip: `pip install coverage`

Con las dependencias ya instaladas, basta con ejecutar los siguientes comandos:
```
coverage run -m pytest
coverage report
```

Obtendrá en pantalla los resultados de las pruebas que se encuentran en el archivo `test_manejador.py` estas pruebas
consiguen una cobertura del 92% sobre todo el código.