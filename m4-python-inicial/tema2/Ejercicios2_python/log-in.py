#Pedir la contraseña por pantalla
user_pass = input('Introduce la contraseña: ')

#Comprobar si la contraseña es correcta
if user_pass.lower() == 'usuario123':
    print('Bienvenido al panel de control')
else:
    if user_pass.lower() != 'usuario123':
        print('Contraseña incorrecta')
        user_pass = input('Introduzca la contraseña de nuevo: ')
        if user_pass.lower() != 'usuario123':
            print('Error, no tienes más intentos')