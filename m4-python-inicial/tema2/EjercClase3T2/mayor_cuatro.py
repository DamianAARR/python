def pedir_numeros():
    # Pide los números al usuario
    numUno = int(input('Introduce un número: '))
    numDos = int(input('Introduce otro número: '))
    numTres = int(input('Introduce otro número: '))
    numCuatro = int(input('Introduce otro número: '))
    #Llamar a la función comprobadora
    mayor = comprobar_mayor(numUno,numDos,numTres,numCuatro)
    
    devolver_resultado(mayor)

def comprobar_mayor(a,b,c,d):
    # Comprueba cuál es el número mayor
    #VERSIÓN DEL PROFE - (Muy práctico para hacer comparaciones. Si se amplía el número de elementos igualmente siempre se imprime el último) Esto es para el mayor
    if (a>b):
        b = a
    if (b>c):
        c = b
    if (c>d):
        d = c
    return d

def devolver_resultado(num_mayor):
    print('El número mayor es,',num_mayor)

#Llamar a la función que pide los números
pedir_numeros()





#VERSIÓN DEL PROFE - Esto mantiene el orden de los valores dados a las letras a la hora de imprimirlo.

""" if (a>b):
    a,b = b,a
if (b>c):
    b,c = c,b
if (c>d):
    c,d = d,c

print('El orden es:', a,b,c,d) """