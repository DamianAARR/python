#Importar librerias
import numpy as np
#Inicializar listas

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

#Extraer fechas (columna 0)
fechas_ventas = np.array([venta[0] for venta in ventas]) #Recorremos cada elemento del array (for venta in ventas) y nos quedamos con el
                                                         #primer elemento de cada lista de ventas (ventas[0])
print(fechas_ventas)
#Extraer los meses de la fecha completa
meses = np.array([int(fecha[5:7]) for fecha in fechas_ventas])#Recorremos cada fecha del nuevo array 'fechas_ventas' (for fecha in fechas_ventas)
                                                         #y nos quedamos con la posición 5:7 de cada elemento (fecha[5:7])
#Sumar los montos de venta de cada mes
montos_mes = np.zeros(12) #Creamos un array lleno de ceros (np.zeros) para almacenar los montos de cada mes (12)

for i in range(1,13): #Recorremos todos los meses (1,13)
    ventas_mes = ventas[meses == i] #La venta de ese mes es el elemento donde meses es igual al su número de mes (meses == i) dentro del array de ventas (ventas[meses = i])
    montos_mes[i-1] = np.sum(ventas_mes[:,1].astype(int)) #Sumamos las ventas de cada mes (np.sum) y las almacenamos en el array 'montos_mes'.
                                                          #El [i-1] es por que los meses empiezan en 1 (1,13) pero el array donde se almacena (montos_mes) empieza en 0.
                                                          #Con ventas_mes[:,1] selecionamos la columna 1 para que solo esos elementos sean sumados.
                                                          #Con '.astype(int)' convertimos los elementos que hay en 'ventas_mes[:,1]' en enteros para poder sumarlos.

