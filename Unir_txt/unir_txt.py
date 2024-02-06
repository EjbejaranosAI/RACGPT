import archivos

from os import walk, getcwd

ruta = 'Ruta de los archivos para unir'
txt_completo = []

path_files = archivos.info_rutas(ruta)
    
num = len(path_files)

for i in range(num):
  with open(path_files[i],'r') as archivo:
    datos = f'data{i} = {repr(archivo.read())}'
    exec(datos)
    txt_completo.append(eval(f'data{i}'))

data = archivos.list_to_json(txt_completo)

with open('Ruta para guardar el archivo', 'w') as archivo:
    rac = '\n'.join(txt_completo)
    rac = rac.replace('[', '').replace(']', '').replace('},', '}').replace('}','},').replace('\n\n','').replace('{\n{','')

    archivo.write(rac)