#Pedir tres números diferentes por pantalla
numUno = int(input('Introduce un número: '))
numDos = int(input('Introduce otro número: '))
numTres = int(input('Introduce otro número: '))

#Comprobar si uno de ellos es la suma de los otros dos
if numUno == (numDos + numTres):
    print('El número', numUno, 'es la suma del numero',numDos, 'y el número',numTres)
elif numDos == (numUno + numTres):
    print('El número', numDos, 'es la suma del numero',numUno, 'y el número',numTres)
elif numTres == (numUno + numDos):
    print('El número', numTres, 'es la suma del numero',numUno, 'y el número',numDos)
else:
    print('Ningún número es la suma de los otros dos')