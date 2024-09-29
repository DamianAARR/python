#Pedir por pantalla el nombre de usuario
usuario = input('Introduce tu usuario: ')

#Solucionar problema de nombre mal escrito 
usuario = usuario.replace(".","")
usuario = usuario.replace(" ","")
usuario = usuario.replace("#","")

#Nombre de usuarios registrados
usuario1 = "alejandro"
usuario2 = "naomi"
usuario3 = "sergio"

#Dar bienvenida personalizada
if usuario.lower() == usuario1 or usuario.lower() == usuario2 or usuario.lower() == usuario3:
    print('Bienvenido',usuario.title(), '!')
else:
    print('Bienvenido usuario invitado')

