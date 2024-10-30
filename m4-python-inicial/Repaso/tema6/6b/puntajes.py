##### FUNCIONES #####
def add_player(datos):
    #Añade jugador y puntos
    datos[input('Nº de jugador:\n')] = {'nombre': input('Nombre:\n'), 'puntos': [int(input('Puntos:\n'))]}
    return datos


def add_score(datos):
    #Añade los puntos del jugador
    datos[input('Nº de jugador:\n')]['puntos'].append(int(input('Introduce los nuevos puntos:\n')))
    return datos    


def show_high_score(datos):
     #Muestra el punto más alto
    higher = 0
    name_higher = ''
    print()
    for info in datos.values():
        if max(info['puntos']) > higher:
            higher = max(info['puntos'])
            name_higher = info['nombre']
    
    print('Puntaje más alto:')
    print('Jugador:',name_higher.title(),'- Puntos:',higher)


def show_mean_score(datos):
    #Muestra la puntuación media general
    puntuaciones = []
    for info in datos.values():
        puntuaciones.append(sum(info['puntos']))
    
    media = sum(puntuaciones) / len(puntuaciones)
    print()
    print('Media de puntajes general:',media,'puntos')


def show_players(datos):
    #Mostrar número de jugadores
    print()
    print('Número de jugadores:',len(datos))
    for info in datos.values():
        print(info['nombre']).title()


##### CASO DE USO #####
continuar = True
database ={}

while continuar:
    print()
    option = input('Elige una opción:\n1.-Añadir jugador\n2.-Añadir puntuación\n3.-Mostrar puntaje más alto\n4.-Mostrar media de puntaje\n5.-Mostrar número de jugadores\n6.-Salir del programa\n')
    
    if option == '1':
        registro = add_player(database)
        print()
        [[print(player)]for player in registro.items()]
    
    if option == '2':
        registro = add_score(registro)
        print()
        [[print(player)]for player in registro.items()]
        
    if option == '3':
        high_score = show_high_score(registro)
        print()
        #[[print(score)]for score in high_score]
    
    if option == '4':
        show_mean_score(registro)
    
    if option == '5':
        show_players(registro)
    
    if option == '6':
        print()
        print('Saliendo del programa')
        print()
        continuar = False