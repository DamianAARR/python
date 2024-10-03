import time
#FUNCIONES
def pedir_password():
    # Pide la contraseña al usuario
    pass_usuario = input('Introduce la contraseña: ')
    return pass_usuario


def comprobar_pass(user_pass):
    # Comprueba si la password coincide con la almacenada
    if user_pass != password:
        validate = False
    else:
        validate = True
    return validate


def mensaje_bienvenida():
    print('Contraseña correcta')
    print()
    time.sleep(1)
    print('Iniciando sesión...')
    time.sleep(1)
    print('---------------------')
    print('BIENVENIDO AL SISTEMA')


#Almacenar la constraseña
password = 'usuario.123'
continuar = True

#Llamar a las funciones dentro del bucle
while continuar:
    user_pass = pedir_password()
    validate = comprobar_pass(user_pass)
    
    if validate:
        mensaje_bienvenida()
        continuar = False
    else:
        print('Contraseña incorrecta, inténtelo de nuevo')

