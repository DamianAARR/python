#Inicializar lista y variables
estudiantes = [['luis',4,7,9],['david',6,3,8],['jesus',4,3,6],['miguel',7,5,9],['javier',8,7,8],['lucas',5,5,5],['antonio',5,8,7],['jorge',10,10,10]]
suma_notas = 0
suma_notas_medias = 0
nota_media_individual = 0
nota_media_clase = 0

#Recorremos cada lista de la lista
for estudiante in estudiantes:
    #Recorremos cada elemento de las listas dentro de la lista
    for i in range(1,len(estudiante)):
        suma_notas = suma_notas + estudiante[i]
    #Sacamos la nota media de cada alumno de la lista
    nota_media_individual = suma_notas / (len(estudiante) - 1)
    #Añadimos la nota media de cada alumno a una nueva variable
    suma_notas_medias = suma_notas_medias + nota_media_individual

    print('Nota media del alumno',str(estudiante[0]).title(),':',nota_media_individual)
    suma_notas = 0

#Calculamos la nota media de la clase y la imprimimos
nota_media_clase = suma_notas_medias / len(estudiantes)
print()
print('Nota media de la clase:',nota_media_clase)
