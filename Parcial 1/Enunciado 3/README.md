# Codigos del Enunciado 3

Estos codigos corresponden a la implementación del simulador del sistema de manejo de memoria "Buddy System" en Python.

Para usarla, necesita descargar Python
de su [página web](https://www.python.org/downloads/)

Se incluyen tanto los archivos de las pruebas unitarias como la clase que maneja al sistema y un cliente para esta clase.

Para poder iniciar el cliente, debe ejecutar el siguiente comando en el directorio: `python Client.py <cantidad_de_memoria>`, donde
`<cantidad_de_memoria>` es un numero entero que representa la cantidad de memoria con la que se inicializa el simulador. Por ejemplo:
```
.> python Client.py 32
```
Esto inicializa el simulador con 32 posibles bloques de memoria.

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

Obtendrá en pantalla los resultados de las pruebas que se encuentran en el archivo `test_BuddySystem.py` estas pruebas
consiguen una cobertura del 95% sobre el código del módulo `BuddySystem`