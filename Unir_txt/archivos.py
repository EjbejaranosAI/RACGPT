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


def list_to_json (file):

  json_data = json.dumps(file, indent=4, ensure_ascii=False)
  print(json_data)

  return json_data
