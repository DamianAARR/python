#PASO22
print('----------')
productos = {
    'prod1': {
        'nombre': 'manzana',
        'precio': 0.76,
    },
    'prod2': {
        'nombre': 'platano',
        'precio': 1.25,
    },
}

#PASO23
print('----------')
productos['prod3'] = {'nombre': 'naranja','precio': 1.10}
print(productos)

#PASO24
print('----------')
equipos = {'team1': {'nombre': 'almu',   'jugadores': ['manuel','carlos','jorge']},
           'team2': {'nombre': 'salo',   'jugadores': ['juan','luis','davis']},
           'team3': {'nombre': 'motril', 'jugadores': ['lucas','miguel','antonio']}
           }
for equipo, info in equipos.items():
    print(info['nombre'].title(),':',info['jugadores'])

#PASO25
print('----------')
equipos['team4'] = {'nombre': 'torrenueva', 'jugadores': ['arturo','joaquin','paquito']}
[[print(info['nombre'].title(),':',info['jugadores'])] for equipo, info in equipos.items()]

#PASO26
print('----------')
equipos['team4']['jugadores'].append('manolillo')
[[print(info['nombre'].title(),':',info['jugadores'])] for equipo, info in equipos.items()]
