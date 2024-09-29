#Crear base de datos vacía
votaciones = {}
continuar = True
suma_votos = 0

#Dar funcionalidad al programa
while continuar:
    opcion = input('1. Registrar candidatos y votos\n2. Mostrar candidatos y votos\n3. Mostrar candidato ganador\n4. Mostrar porcentaje de votos\n5. Salir del programa\n')

    # Registrar candidatos y votos
    if opcion == '1':
        nombre = input('Introduce el nombre del candidato: ')
        if nombre.lower() in votaciones:
            nombre = input('Este candidato ya está registrado, introduzca uno nuevo:')
            votos = int(input('Introduce el número de votos:'))
            votaciones[nombre] = votos
        else:
            votos = int(input('Introduce el número de votos:'))
            votaciones[nombre] = votos
            print()

    # Mostrar lista de candidatos y los votos
    elif opcion == '2':
        print()
        print('Lista de candidatos:')
        for candidato, votos in votaciones.items():
            print(candidato.title(),':',votos,'votos')
        print()

    # Mostrar candidato ganador
    elif opcion == '3':
        print()
        for candidato, votos in votaciones.items():
            ganador = max(votaciones, key=votaciones.get)
            votos_ganador = max(votaciones.values())
        print('El candidato ganador es',ganador.title(),'con',votos_ganador,'votos')
        print()
        
    # Mostrar candidato ganador
    elif opcion == '4':
        print()
        # Obtener votos totales
        for votos in votaciones.values():
            suma_votos += votos

        for candidato, votos in votaciones.items():
            porcentaje = (votos * 100) / suma_votos
            print(candidato.title(),':',round(porcentaje,2),'%','de los votos')
        print()

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