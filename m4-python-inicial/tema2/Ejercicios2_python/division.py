#Pedir por pantalla dos numeros
numUno = int(input('Introduce un numero entero'))
numDos = int(input('Introduce otro numero entero'))

#Calcular su división
if numDos > 0:
    division = numUno / numDos
    print('El resultado de la división es:',division)
else:
    print('Error: No se puede dividir entre 0')