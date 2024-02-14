"""
Descripcion: Este diccionario almacena las imagenes PNG de troncos en el inventario o suelo, no arboles, ya eso es
para el diccionario src/images/trees.py
"""

import os

absolute_path = os.path.dirname(__file__)

logs = {
    'simple': {
        '1':  os.path.join(absolute_path,'../../img/logs/logs.png')
    }
}