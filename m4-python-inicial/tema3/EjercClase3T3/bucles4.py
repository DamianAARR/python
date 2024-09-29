#Pedir por pantalla una frase y una letra
frase = input('Introduce una frase: ')
letra = input('Introduce una letra: ')

#Inicializar variables
cantidad = 0

#Comprobar el número de veces que aparece la letra en la frase

for i in range(0,len(frase)):
    if frase[i] == letra:
        cantidad = cantidad + 1

#Devolver el número de veces que aparece
print()
print('La letra',letra,'aparece',cantidad,'veces en la frase:',frase)
