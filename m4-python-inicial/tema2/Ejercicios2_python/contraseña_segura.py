

#Pedir por pantalla la contraseña
contrasena = input('Introduce tu contraseña')

#Comprobar si la contraseña es segura y decirselo al usuario
if ('a' in contrasena or 'e' in contrasena or 'i' in contrasena or 'o' in contrasena or 'u' in contrasena) and '*' in contrasena and '#' in contrasena:
    print('La contraseña es muy segura')
else:
    print('La contraseña no es segura, tienes que mejorarla')

