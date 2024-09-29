#Inicializar listas y variables
ventas = [120,80,140,200,75,100,180,220,160,110,90,120,170,190,250,300,95,110,140,180,200,160,120,80,170,150,210,190,230,250]
dias_semana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
ventas_dia =[]
dia = 0
mas_ventas = []

#Recorrer ventas y sumar
for i in range(0,len(ventas)):
    #Si la lista 'ventas_dia' tienes menos de 7 entradas añadimos los 7 primeros números de la lista 'ventas'
    if len(ventas_dia) < 7:
        ventas_dia.append(ventas[i])
        #Una vez que ya tiene 7 entradas vamos reemplazando los valores por la suma total de las ventas de ese día
    elif len(ventas_dia) == 7:
        ventas_dia[dia] = ventas_dia[dia] + ventas[i]
        dia = dia + 1
        #Cuando el día llegue a 7 lo reiniciamos a 0 para que vuelva al principio de la lista
        if dia == 7:
            dia = 0

#Creamos una lista anidada con los dias de la semana y las ventas totales del día. Añadimos primero el número de ventas para el siguiente paso.
for i in range(0,len(dias_semana)):
    mas_ventas.append([ventas_dia[i],dias_semana[i]])

#Ordenamos la lista por orden numérico.
mas_ventas.sort()
#Invertimos la lista para tenerla en orden de mayor a menor
mas_ventas.reverse()

#[[980, 'Lunes'], [910, 'Martes'], [760, 'Domingo'], [660, 'Sábado'], [570, 'Jueves'], [485, 'Viernes'], [425, 'Miércoles']]

#---Devolvemos los resultados del análisis---
print('Ventas por día:')
#Imprimimos las ventas totales de cada día de la semana
for i in range(0,len(dias_semana)):
    print(dias_semana[i],ventas_dia[i])
print('-------------------------------------------------')

#Imprimimos los días de la semana en orden ascendente de ventas totales para saber qué días se vende más
print('Días por orden de más venta:')
for i in range(0,len(mas_ventas)):
    print(mas_ventas[i][1],mas_ventas[i][0])