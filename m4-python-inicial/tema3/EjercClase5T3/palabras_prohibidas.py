#Crear listas
palabras = ['covid','vacuna','magrebi','robo','estafa']
letras_prohibidas = ['s','a','t']
filtradas = []
contiene = False

#Recorremos cada elemento de la lista
for i in range(0,len(palabras)):
    #Recorremos las diferentes letras de cada palabra de la lista
    for letra in palabras[i]:
        #Comprobamos si alguna letra está en la lista de letras prohibidas
        if letra in letras_prohibidas:
            contiene = True
    if contiene == False:
        filtradas.append(palabras[i])
    contiene = False

print(filtradas)