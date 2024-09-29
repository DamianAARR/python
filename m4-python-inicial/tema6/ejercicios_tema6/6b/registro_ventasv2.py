#Crear database vacía
ventas_diarias = {}
suma_ventas = 0

#Funcionalidad del programa
continuar = True
while continuar:
    opcion = input('1. Introducir producto y cantidad\n2. Actualizar cantidad de un producto\n3. Saber total de ventas diarias\n4. Salir\n')
    #Añadir producto y cantidad
    if opcion == '1':
        nombre = input('Introduce el nombre del producto:')
        if nombre.lower() in ventas_diarias:
            nombre = input('Ese producto ya está registrado, introduzca uno nuevo:')
            cantidad = int(input('Introduce la cantidad vendida:'))
        else:
            cantidad = int(input('Introduce la cantidad vendida:'))
            ventas_diarias[nombre] = cantidad
            print()
            for producto, cantidad in ventas_diarias.items():
                print(producto.title(),':',cantidad)
            print()
    #Actualizar cantidad
    elif opcion == '2':
        print()
        for producto, cantidad in ventas_diarias.items():
            print(producto.title(),':',cantidad)
        print()
        producto = input('Introduce el nombre del producto que quieres actualizar:')
        if producto.lower() in ventas_diarias:
            nueva_cantidad = int(input('Introduce la nueva cantidad:'))
            ventas_diarias[producto] = nueva_cantidad
            print()
            for producto, cantidad in ventas_diarias.items():
                print(producto.title(),':',cantidad)
            print()
        else:
            print()
            print('Ese producto no está registrado en las ventas diarias, primero debe registrarlo (Opción 1)')
            print()

    #Calcular total de ventas diarias
    elif opcion == '3':
        for cantidad in ventas_diarias.values():
            suma_ventas += cantidad
        #Devolver el total de ventas diarias
        print()
        print('Total de ventas diarias:',suma_ventas,'ventas')
        print()
    
    #Salir del programa
    elif opcion == '4':
        continuar = False
        print()
        print('Saliendo del programa...')
        print()
    #No es una opción correcta
    else:
        print()
        print('Esa opción no es válida, por favor seleccione una opción válida.')
        print()

