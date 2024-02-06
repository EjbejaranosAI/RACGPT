import archivos
import json

from os import walk, getcwd

ruta = 'Ruta de los archivos para unir'

txt_completo = []

path_files = archivos.info_rutas(ruta)
    
for path_file in path_files:
  with open(path_file, "r") as archivo:  
    data_json = json.load(archivo)
    txt_completo.extend(data_json)

ruta_guardado = 'Ruta para guardar el archivo'

with open(ruta_guardado, 'w') as archivo_unido:
  json.dump(txt_completo,archivo_unido,  indent=4)

