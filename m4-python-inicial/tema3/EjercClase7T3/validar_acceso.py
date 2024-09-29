#Inicializar listas y variables
usuarios = ['juan123','ana456','pedro789']
contraseñas = ['clave123','clave456','clave789']
acceso = False

#Pedir al usurio que introduzca su nombre y contraseña
nombreUsuario = input('Introduce tu usuario: ')
contraseñaUsuario = input('Introduce tu contraseña: ')

#Comprobamos si la el usuario y la contraseña tienen la misma posición en sus respectivas listas
for i in range(0,len(usuarios)):
    for j in range(0,len(contraseñas)):
        if nombreUsuario == usuarios[i] and contraseñaUsuario == contraseñas[j]:
            #Guardamos los índices donde coinciden
            posicionUsuario = i
            posicionContraseña = j
            
#Si los índices coinciden los datos introducidos son correctos
if posicionUsuario == posicionContraseña:
    print('Datos correctos')
else:
    print('Los datos no coinciden')



