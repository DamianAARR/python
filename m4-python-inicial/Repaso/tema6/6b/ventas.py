##### FUNCIONES #####
def registrar_ventas(registro):
    #Permite registrar las ventas en el diccionario
    registro[input('Nº de producto: ')] =  {'nombre': input('Nombre del producto: \n'), 'cantidad': int(input('Cantidad vendida:'))}
    return registro


def actualizar_cantidad(datos):
    #Permite actualizar la cantidad vendida de cada producto
    datos[input('Nº de producto: ')] =  {'nombre': input('Nombre del producto: \n'), 'cantidad': int(input('Cantidad nueva:'))}
    return datos


def consultar_ventas(datos):
    #Consulta las ventas totales diarias
    ventas_diarias = []
    for info in datos.values():
        ventas_diarias.append(int(info['cantidad']))

    total = sum(ventas_diarias)
    return total
    

##### CASO DE USO #####
continuar = True
registro = {}

while continuar:
    print()
    option = input('Elige una opción:\n1.- Registrar venta\n2.- Actualizar cantidad vendida\n3.- Total de ventas diarias\n4.- Salir\n')
    print()

    if option == '1':
        datos = registrar_ventas(registro)
        print()
        [[print(prod)]for prod in datos.items()]

    if option == '2':
        datos = actualizar_cantidad(datos)
        print()
        [[print(prod_act)]for prod_act in datos.items()]
        
    if option == '3':
        ventas = consultar_ventas(datos)
        print()
        print('Ventas totales del día:',ventas)
        

    if option == '4':
        print('Saliendo del programa')
        print()
        continuar = False
        


