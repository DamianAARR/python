#Inicializar variables y listas
numeros = [1,5,8,3,68,32,67,85,15,65]
suma = 0

#Pedir al usuario un número por consola
numUsuario = int(input('Introduce un número entero: '))

for i in range(0,len(numeros)):
    if numeros[i] % numUsuario == 0:
        suma = suma + numeros[i]

#Devolver la respuesta
print('La suma de los números de la lista divisibles por',numUsuario,'es',suma)