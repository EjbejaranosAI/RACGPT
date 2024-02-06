import os
import json

from os import walk, getcwd

def info_rutas(ruta):
    path = []
    for dirpath, dirnames, filenames in os.walk(ruta):  # Recorre el directorio y sus subdirectorios
        for filename in filenames:

            rutas = os.path.join(dirpath, filename)     # Une los componentes formando la ruta de acceso al archivo
            path.append(rutas)

    return path

