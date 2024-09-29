#Pedir por pantalla dos numeros
numUsuario = int(input('Introduce un numero entero'))
potencia = int(input('Introduce la potencia al que elevarlo'))

#Calcular si es par o impar
if (numUsuario**potencia) % 2 == 0:
    print('El número',numUsuario,'elevado a',potencia,'es par')
else:
    print('El número',numUsuario,'elevado a',potencia,'es impar')

