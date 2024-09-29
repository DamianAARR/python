#Inicializar variables y listas
numeros = [1,5,8,3,68,32,67,85,15,65]
numeroAlto = 0

#Pedir al usuario un número por consola
numUsuario = int(input('Introduce un número entero: '))

#Bucle para recorrer la lista

for i in range(0,len(numeros)):
    if numUsuario > numeros[i] > numeroAlto:
        numeroAlto = numeros[i]

#Devolver respuesta
print('El número más alto de la lista por debajo del número introducido es:',numeroAlto)

