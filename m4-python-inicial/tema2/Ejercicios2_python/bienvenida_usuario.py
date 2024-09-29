#Pedir por pantalla el nombre de usuario
usuario = input('Introduce tu usuario: ')

#Solucionar problema de nombre mal escrito 
usuario = usuario.replace(".","")
usuario = usuario.replace(" ","")
usuario = usuario.replace("#","")

#Dar bienvenida personalizada

if usuario.lower() == 'alejandro':
    print('Bienvenido,',usuario.title())
elif usuario.lower() == 'naomi':
    print('Bienvenida,',usuario.title())
elif usuario.lower() == 'sergio':
    print('Bienvenido,',usuario.title())
else:
    print('Usuario desconocido')