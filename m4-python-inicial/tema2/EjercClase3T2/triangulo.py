#Pedir por pantalla las longitudes de los lados
longUno = float(input('Introduce una longitud: '))
longDos = float(input('Introduce otra longitud: '))
longTres = float(input('Introduce otra longitud: '))

#Comprobar si podría construirse el triángulo
if (longUno < (longDos + longTres)) and (longDos < (longUno + longTres)) and (longTres < (longUno + longDos)):
    print()
    print('SI podría construir un triángulo')
    print()
else:
    print()
    print('NO podría construir un triángulo')
    print()