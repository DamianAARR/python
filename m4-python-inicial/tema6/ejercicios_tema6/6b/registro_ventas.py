#Crear base de datos (Diccionario vacío)
ventas_diarias = {}
ventas_producto = []
actualizar = False
#Rellenar diccionario vacío
num_productos = int(input('¿Cuántos productos diferentes se han vendido hoy?:'))

for i in range(num_productos):
    ventas_diarias[input('Introduce el número de producto:')] = {'nombre': input('Introduce el nombre del producto:'), 'cantidad': int(input('Introduce la cantidad vendida:'))}
    print()
#Devolver base de datos ventas diarias
print()
print('--Ventas diarias:--')
for producto, info_producto in ventas_diarias.items():
    print(producto, info_producto)
    print()

#Opción de actualizar cantidad vendida de un producto
pregunta = input('¿Quieres actualizar la cantidad de un producto?:')
if pregunta == 'si':
    actualizar = True
    while actualizar == True:
        ventas_diarias[input('Introduce el número de producto a actualizar:')]['cantidad'] = int(input('Introduce la nueva cantidad:'))
        print('--Ventas diarias:--')
        for producto, info_producto in ventas_diarias.items():
            print(producto, info_producto)
            print()
        pregunta = (input('¿Quieres actualizar otro producto?:'))
        if pregunta == 'no':
            actualizar = False
else:
    actualizar = False

#Calcular las ventas totales diarias
for info in ventas_diarias.values():
    ventas_producto.append(info['cantidad'])
suma_ventas = sum(ventas_producto)

#Devolver ventas totales diarias
print()
print('Total de ventas diarias:',suma_ventas)




    

