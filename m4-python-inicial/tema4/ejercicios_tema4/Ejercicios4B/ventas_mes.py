#Importar librerias
import numpy as np
#Inicializar listas
fechas_clean_str = []
fechas_int = []
ventas_enero = []
ventas_febrero = []
ventas_marzo = []

#Datos de ventas de la tienda
ventas = np.array([
    ['2022-01-01',100,'ropa'],
    ['2022-01-02',200,'alimentos'],
    ['2022-01-03',150,'ropa'],
    ['2022-02-01',120,'alimentos'],
    ['2022-02-02',180,'electronicos'],
    ['2022-02-03',200,'alimentos'],
    ['2022-03-01',90,'ropa'],
    ['2022-03-02',110,'electronicos'],
    ['2022-03-03',100,'alimentos']
])

#fechas_clean = str(ventas[:,0]).replace('-','')
#Extraer fechas (columna 0)
fechas_guion = ventas[:,0]
#Pasar fechas de numpy.str a str y quitar guiones
for i in range(0,len(fechas_guion)):
    fechas_clean_str.append(str(fechas_guion[i]).replace('-',''))
#Pasar las fechas de elemento 'str' a elemento 'int'
for i in range(0,len(fechas_clean_str)):
    fechas_int.append(int(fechas_clean_str[i]))

print(fechas_clean_str)


for i in range(0,len(fechas_clean_str)):
    fecha = fechas_clean_str[i]
    if fecha[4:6] == '01':
        ventas_enero.append(int(ventas[i][1]))
    if fecha[4:6] == '02':
        ventas_febrero.append(int(ventas[i][1]))
    if fecha[4:6] == '03':
        ventas_marzo.append(int(ventas[i][1]))

print('Monto total Enero:',sum(ventas_enero))
print('Monto total Febrero:',sum(ventas_febrero))
print('Monto total Marzo:',sum(ventas_marzo))

