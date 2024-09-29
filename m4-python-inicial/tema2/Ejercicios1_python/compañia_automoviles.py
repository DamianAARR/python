#Pedir por pantalla el número de coches vendidos
print('Cuantos conches Serie 1 has vendido?')
num_serie1 = int(input())
print('Cuantos conches Serie plus has vendido?')
num_serieplus = int(input())
print('Cuantos conches todoterreno has vendido?')
num_todoterreno = int(input())

#Calcular las comisiones del mes
precio_serie1 = 20000
precio_serieplus = 35000
precio_todoterreno = 60000

comision_serie1 = num_serie1 * precio_serie1 * 0.03
comision_serieplus = num_serieplus * precio_serieplus * 0.05
comision_todoterreno = num_todoterreno * precio_todoterreno * 0.07

comision_mensual = comision_serie1 + comision_serieplus + comision_todoterreno

#Devolver la cantidad en euros
print('Este mes recibes un total de', comision_mensual, 'euros por las comisiones.')