#Pedir usuario por consola
usuario = input('Introduce tu usuario')

if usuario == 'administrador':
    print('Bienvenido al panel de control del sistema, como administrador tienes acceso completo a todas las opciones')
else: 
    print('Bienvenido,',usuario.title())