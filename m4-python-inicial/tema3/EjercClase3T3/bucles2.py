import time

#Almacenar la constraseña
password = 'usuario.123'
correcta = False

#Pedir por pantalla que introduzca la contrasña
while correcta == False:
    pass_usuario = input('Introduce la contraseña: ')
    if pass_usuario != password:
        print('Contraseña incorrecta.')
    else:
        correcta = True


#Mensaje bienvenida
print('Contraseña correcta')
print()
time.sleep(1)
print('Iniciando sesión...')
print()
time.sleep(1)
print()
print('---------------------')
print('BIENVENIDO AL SISTEMA')