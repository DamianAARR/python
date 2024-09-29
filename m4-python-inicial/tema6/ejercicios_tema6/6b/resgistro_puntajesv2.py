seguimiento = {}
puntaje = []
seguir = True

#Dar funcionalidad para añadir nombre y puntaje
while seguir == True:
    nombre = input('Introduce tu nombre:')
    mas_puntos = True
    while mas_puntos == True:
        punto = (int(input('Introduce tus puntos:')))
        puntaje.append(punto)
        introducir_más = input('¿Introduces más puntos? (si o no):')
        if introducir_más == 'si':
            mas_puntos = True
        else:
            mas_puntos = False
        seguimiento[nombre] = puntaje
    puntaje = []
    nuevo_usuario = input('¿Introducir nuevo usuario?: (si o no)')
    if nuevo_usuario == 'si':
        seguir = True
    else:
        seguir = False

#Presentar base de datos
for jugador, puntaje in seguimiento.items():
    print(jugador.title(),':',*puntaje)

#Dar fundionalidad para acceder a los datos
seguir = True
while seguir == True:
    nombre = input('Introduce tu nombre para consultar datos:')
    dato = input('Que quieres consultar? (puntaje alto, promedio, jugadores)')
    if dato == 'puntaje alto':
        print('Tu puntaje más alto:',max(seguimiento[nombre]))
    elif dato == 'promedio':
        media_puntajes = sum(seguimiento[nombre]) / len(seguimiento[nombre])
        print('Tu puntaje medio:',round(media_puntajes,2))
    elif dato == 'jugadores':
        print('Total de jugadores:', len(seguimiento))
    nueva_consulta = input('¿Quieres consultar algo más?: (si o no)')
    if nueva_consulta == 'si':
        seguir = True
    else:
        seguir = False




