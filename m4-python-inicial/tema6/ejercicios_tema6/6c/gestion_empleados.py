#Crear base de datos vacía
empleados = {}
continuar = True
suma_salarios = 0
num_empleados_depart = 0

#Dar funfionalidad al programa
while continuar:
    opcion = input('1. Agregar empleado\n2. Actualizar salario\n3. Lista de empleados\n4. Promedio salario por departamento\n5. Salir del programa\n')

    # Añadir empleado
    if opcion == '1':
        nombre = input('Introduce el nombre: ')
        if nombre.lower() in empleados:
            nombre = input('Este empleado ya está registrado, introduzca uno nuevo:')
            salario = int(input('Introduce el salario:'))
            departamento = input('Introduce el departamento:')

            empleados[nombre] = {'salario': salario, 'departamento': departamento}

            print()
            for empleado, datos in empleados.items():
                print(empleado.title(),':',datos)
            print()
        else:
            salario = int(input('Introduce el salario:'))
            departamento = input('Introduce el departamento:')
            empleados[nombre] = {'salario': salario, 'departamento': departamento}
            print()
            for empleado, datos in empleados.items():
                print(empleado.title(),':',datos)
            print()

    # Actualizar salario
    elif opcion == '2':
        print()
        for empleado, datos in empleados.items():
            print(empleado.title(),':',datos)
        print()

        empleado = input('Introduce el nombre del empleado: ')
        if empleado.lower() in empleados:
            salario = int(input('Introduce el nuevo salario: '))
            empleados[empleado]['salario'] = salario
            print()
            for empleado, datos in empleados.items():
                print(empleado.title(),':',datos)
            print()
        else:
            print()
            print('Ese empleado no está registrado, primero debe registrarlo (Opción 1)')
            print()

    # Mostrar lista de empleados
    elif opcion == '3':
        print()
        print('Lista de empleados:')
        for empleado in empleados:
            print(empleado.title())
        print()

    # Calcular promedio salarial por departamento
    elif opcion == '4':
        print()
        depart = input('Introduce el departamento: ')
        if depart in datos['departamento']:
            for empleado, datos in empleados.items():
                if depart.lower() == datos['departamento'].lower():
                    suma_salarios += datos['salario']
                    num_empleados_depart += 1
                    promedio_salarial = suma_salarios / num_empleados_depart
            print()
            print('El departamento de',depart.title(),'tiene un promedio salarial de',round(promedio_salarial,2),'euros')
        else:
            print()
            print('No existe ese departamento, prueba con otro.')
            
        print()
        #Devolver el total de ventas diarias
        
    # Salir del programa
    elif opcion == '5':
        continuar = False
        print()
        print('Saliendo del programa...')
        print()
    #No es una opción correcta
    else:
        print()
        print('Esa opción no es válida, por favor seleccione una opción válida.')
        print()

