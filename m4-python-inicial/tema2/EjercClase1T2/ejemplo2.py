# FUNCIONES
def comprobar_numero(numUsuario):
    if (numUsuario % 3 == 0):
        print('El número',numUsuario,'es múltiplo de 3')
    else:
        print('El número',numUsuario,'NO es múltiplo de 3')

#Pedir número por pantalla
numUsuario = int(input('Introduce un número entero'))

#Comprobar si es múltiplo de 3
comprobar_numero(numUsuario)
