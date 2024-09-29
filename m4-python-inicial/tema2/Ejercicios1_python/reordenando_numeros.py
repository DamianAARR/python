#Pedir por consola un número de más de una cifra
print('Introduce un número de más de una cifra')
numUsuario = input()


#Imprimir cada cifra de forma individual
print(*numUsuario, sep='\t')

#Imprimir el número introducido leído al revés
print(numUsuario[::-1])