#Inicializar listas y variables
usuarios = ['juan123','ana456','pedro789']
contraseñas = ['clave123','clave456','clave789']
acceso = False

#Pedir al usurio que introduzca su nombre y contraseña
nombreUsuario = input('Introduce tu usuario: ')
contraseñaUsuario = input('Introduce tu contraseña: ')

#Comprobamos si la el usuario y la contraseña tienen la misma posición en sus respectivas listas
for i in range(0,len(usuarios)):
    if nombreUsuario == usuarios[i] and contraseñaUsuario == contraseñas[i]:
        acceso = True

if acceso == True:
    print('Datos correctos')
else:
    print('Los datos no coinciden')
        