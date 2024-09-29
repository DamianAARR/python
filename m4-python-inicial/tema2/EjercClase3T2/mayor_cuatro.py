#Pedir por pantalla cuatro números diferentes
numUno = int(input('Introduce un número: '))
numDos = int(input('Introduce otro número: '))
numTres = int(input('Introduce otro número: '))
numCuatro = int(input('Introduce otro número: '))

#Comprobar cual es el mayor

if (numUno > numDos) and (numUno > numTres) and (numUno > numCuatro):
    print('El numero mayor es el', numUno)
elif (numDos > numUno) and (numDos > numTres) and (numDos > numCuatro):
    print('El numero mayor es el', numDos)
elif (numTres > numUno) and (numTres > numDos) and (numTres > numCuatro):
    print('El numero mayor es el', numTres) 
else:
    print('El numero mayor es el', numCuatro) 

#VERSIÓN DEL PROFE - (Muy práctico para hacer comparaciones. Si se amplía el número de elementos igualmente siempre se imprime el último) Esto es para el mayor

if (a>b):
    b = a
if (b>c):
    c = b
if (c>d):
    d = c

print('El mayor de los cuatro es', d)

#VERSIÓN DEL PROFE - Esto mantiene el orden de los valores dados a las letras a la hora de imprimirlo.

if (a>b):
    a,b = b,a
if (b>c):
    b,c = c,b
if (c>d):
    c,d = d,c

print('El orden es:', a,b,c,d)