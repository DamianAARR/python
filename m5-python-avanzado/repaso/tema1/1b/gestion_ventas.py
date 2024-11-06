##### FUNCIONES #####
def agregar_producto(nombre, precio, datos):
    #Agregar producto y precio
    datos.append({'Producto': nombre, 'Precio': precio})
    return datos


def mostrar_ventas(datos):
    #Mostrar las ventas con precios
    for prod in datos:
        print(prod)


##### CASO DE USO #####
database = []
continuar = True

while continuar:
    option = input('Introduce una opción:\n1.-Agregar producto\n2.-Mostrar lista de ventas\n3.-Salir del programa\n')

    if option == '1':
        nombre = input('Nombre del producto:\n')
        precio = input('Precio del producto:\n')
        registro = agregar_producto(nombre,precio,database)

    if option == '2':
        mostrar_ventas(registro)

    if option == '3':
        print()
        print('Saliendo del programa')
        print()
        continuar = False