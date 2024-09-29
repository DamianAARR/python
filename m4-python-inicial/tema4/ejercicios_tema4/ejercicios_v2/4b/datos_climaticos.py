#Importar librerias
import numpy as np

#Datos del clima
clima = np.array([
#    T   H    P    M
    [20, 70, 1009, 1],
    [21, 60, 1011, 1],
    [22, 40, 1010, 1],
    [18, 75, 1012, 2],
    [21, 60, 1008, 3],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [27, 49, 1007, 5],
    [29, 50, 1007, 5],
    [28, 51, 1007, 5],
    [30, 45, 1005, 6],
    [10, 30, 1005, 6],
    [32, 40, 1002, 7],
    [33, 35, 1001, 8],
    [31, 45, 1003, 9],
    [30, 42, 1001, 9],
    [29, 42, 1002, 9],
    [35, 43, 1001, 9],
    [28, 50, 1006, 10],
    [25, 60, 1010, 11],
    [27, 59, 1012, 11],
    [24, 58, 1011, 11],
    [22, 70, 1011, 12]
])

# extraer datos 
meses = np.array(clima[:,3])

#filtrar los datos por meses
temp_media = np.zeros(12)
hum_media = np.zeros(12)
pres_media = np.zeros(12)

for i in range(1,13):
    datos_mes = clima[meses == i]
    temp_media[i-1] = np.mean(datos_mes[:,0]).round(1)
    hum_media[i-1] = np.mean(datos_mes[:,1]).round(1)
    pres_media[i-1] = np.mean(datos_mes[:,2])

for i in range(0,12):
    print('Medias mes',*{i+1},':','-Temp:',temp_media[i],'-Hum:',hum_media[i],'-Pres:',pres_media[i])

presion_media_anual = np.mean(clima[:,2]).round(2)
print()
print('Presión media anual:',presion_media_anual)