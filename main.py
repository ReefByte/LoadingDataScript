import os
import pandas as pd

#Cositas a tener en cuenta:
# 1. ¿Cuál sería la dirección del directorio en donde cargarían las cositas?
#    1.1. ¿Es al Cluster?
# 2. ¿Cuál será su capacidad máxima?

directorio = '/Users/juanf/PycharmProjects/insertCSVScript/'
archivos_csv = []

for archivo in os.listdir(directorio):
    if archivo.endswith('.csv'):
        archivos_csv.append(archivo)

for archivo_csv in archivos_csv:
    print(f'Leyendo archivo: {archivo_csv}')
    ruta_completa = os.path.join(directorio, archivo_csv)
    df = pd.read_csv(ruta_completa)
    print(df)
    print('-' * 50)