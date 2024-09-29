#Paso22
productos = {
    'producto1': {
        'nombre': 'toalla',
        'precio': 10,
    },
    'producto2': {
        'nombre': 'jabon',
        'precio': 5,
    },
}

for producto,producto_info in productos.items(): 
    print(producto_info['nombre'].title(),':',producto_info['precio'],'euros')

#Paso23
productos['producto3'] = {
        'nombre': 'espejo',
        'precio': 20,
    }
print('------')
for producto,producto_info in productos.items(): 
    print(producto_info['nombre'].title(),':',producto_info['precio'],'euros')

#Paso24
equipos = {
    'equipo1': {
        'nombre': 'real madrid',
        'jugadores': ['lucas', 'pedro','miguel']
    },
    'equipo2': {
        'nombre': 'barcelona',
        'jugadores': ['manu', 'juan','david']
    },
    'equipo3': {
        'nombre': 'valladolid',
        'jugadores': ['luis', 'antonio','manolo']
    }
}
print('------')
for equipo, info_equipos in equipos.items():
    print(info_equipos['nombre'].title(),':',*info_equipos['jugadores'])

#Paso25
equipos['equipo4'] = {
    'nombre': 'villareal',
    'jugadores': ['carlos', 'jorge','andrés']
}

print('------')
for equipo, info_equipos in equipos.items():
    print(info_equipos['nombre'].title(),':',*info_equipos['jugadores'])


#Paso26
equipos['equipo1']['jugadores'] = ['lucas', 'pedro','miguel','arturo']

print('------')
for equipo, info_equipos in equipos.items():
    print(info_equipos['nombre'].title(),':',*info_equipos['jugadores'])

