#Crear lista de caracteres
palabras = ['A5','B4','C3','A8','D7','B5']
puntos = []

#Bucle que recorra todos los elementos de la lista
for carta in palabras:
    #Recorrer caracter del string y comprobar si es un número
    for num in carta:
        if num.isdigit() == True:
            #Añadimos los puntos de cada carta a la lista 'puntos' convirtiéndolos en int
            puntos.append(int(num))

print('Mano:',palabras)
print('Puntos totales:',sum(puntos))