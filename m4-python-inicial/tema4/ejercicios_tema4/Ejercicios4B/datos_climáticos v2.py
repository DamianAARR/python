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

#Temperatura, humedad y presión promedio por año
#Calcular la media de todas las columnas
media_general = clima.mean(0)

#Devolver las medias de forma individual
print('Temperatura promedio anual:',media_general[0].round(2))
print('Humedad promedio anual:',media_general[1].round(2))
print('Presión promedio anual:',media_general[2].round(2))

#Temperatura, humedad y presión promedio por mes
#Extraer los meses
meses = np.array([medicion[3]for medicion in clima])

#Medias por mes
media_t_mes = np.zeros(12)
media_h_mes = np.zeros(12)
media_p_mes = np.zeros(12)

for i in range(1,13):
    mediciones_mes = clima[meses == i]
    media_t_mes[i-1] = np.mean(mediciones_mes[:,0]).round(2)
    media_h_mes[i-1] = np.mean(mediciones_mes[:,1]).round(2)
    media_p_mes[i-1] = np.mean(mediciones_mes[:,2])

print('-------')
print('Media de temperatura,humedad y presión por mes:')
for i in range(1,13):
    print('Mes',*[i],':',media_t_mes[i-1],media_h_mes[i-1],media_p_mes[i-1])