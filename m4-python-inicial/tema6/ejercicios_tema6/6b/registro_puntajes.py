#Crear database vacía (Diccionario)
seguimiento = {}
media_puntajes = 0
#Añadir nombre y puntos
seguimiento['jugador1'] = {'nombre':'juan','puntos':[13,34,66]}
seguimiento['jugador2'] = {'nombre':'lucas','puntos':[43,34,12]}
seguimiento['jugador3'] = {'nombre':'pepe','puntos':[21,65,98]}
print()
#Devolver punto más alto, promedio y cantidad jugadores
for info_jugador in seguimiento.values():
    print('Jugador:',info_jugador['nombre'].title())
    print('Puntaje más alto:',max(info_jugador['puntos']))
    media_puntajes = sum(info_jugador['puntos']) / len(info_jugador['puntos'])
    print('Pormedio puntajes:',round(media_puntajes,2))
    media_puntajes = 0
    print() 

print('Jugadores totales:',len(seguimiento))

