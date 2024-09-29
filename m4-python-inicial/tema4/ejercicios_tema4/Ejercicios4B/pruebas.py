#Importar librerias
import numpy as np

#Datos del clima
clima = np.array([
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

#Temperatura, humedad y presión promedio por mes

#Filtrar por número de mes y añadir datos a nuevo array
mes_enero = clima[clima[:, 3] == 1] 
mes_febrero = clima[clima[:, 3] == 2]
mes_marzo = clima[clima[:, 3] == 3] #Marzo es igual a clima en las posiciones en las que el valor del índice 3 es 3
mes_abril = clima[clima[:, 3] == 4]
mes_mayo = clima[clima[:, 3] == 5]
mes_junio = clima[clima[:, 3] == 6]
mes_julio = clima[clima[:, 3] == 7]
mes_agosto = clima[clima[:, 3] == 8]
mes_septiembre = clima[clima[:, 3] == 9]
mes_octubre = clima[clima[:, 3] == 10]
mes_noviembre = clima[clima[:, 3] == 11]
mes_diciembre = clima[clima[:, 3] == 12]

#Eliminar la columna que indica el mes
mes_enero = np.delete(mes_enero,3,axis=1)
mes_febrero = np.delete(mes_febrero,3,axis=1)
mes_marzo = np.delete(mes_marzo,3,axis=1)
mes_abril = np.delete(mes_abril,3,axis=1)
mes_mayo = np.delete(mes_mayo,3,axis=1)
mes_junio = np.delete(mes_junio,3,axis=1)
mes_julio = np.delete(mes_julio,3,axis=1)
mes_agosto = np.delete(mes_agosto,3,axis=1)
mes_septiembre = np.delete(mes_septiembre,3,axis=1)
mes_octubre = np.delete(mes_octubre,3,axis=1)
mes_noviembre = np.delete(mes_noviembre,3,axis=1)
mes_diciembre = np.delete(mes_diciembre,3,axis=1)

#Calcular la media de cada mes
media_enero = mes_enero.mean(0)
media_febrero = mes_febrero.mean(0)
media_marzo = mes_marzo.mean(0)
media_abril = mes_abril.mean(0)
media_mayo = mes_mayo.mean(0)
media_junio = mes_junio.mean(0)
media_julio = mes_julio.mean(0)
media_agosto = mes_agosto.mean(0)
media_septiembre = mes_septiembre.mean(0)
media_octubre = mes_octubre.mean(0)
media_noviembre = mes_noviembre.mean(0)
media_diciembre = mes_diciembre.mean(0)


print("Datos promedios por meses:")
print('-----------  T  -  H  -  P')
print('Enero:     ',*media_enero.round(2))
print('Febrero:   ',*media_febrero.round(2))
print('Marzo:     ',*media_marzo.round(2))
print('Abril:     ',*media_abril.round(2))
print('Mayo:      ',*media_mayo.round(2))
print('Junio:     ',*media_junio.round(2))
print('Julio:     ',*media_julio.round(2))
print('Agosto:    ',*media_agosto.round(2))
print('Septiembre:',*media_septiembre.round(2))
print('Octubre:   ',*media_octubre.round(2))
print('Noviembre: ',*media_noviembre.round(2))
print('Diciembre: ',*media_diciembre.round(2))



