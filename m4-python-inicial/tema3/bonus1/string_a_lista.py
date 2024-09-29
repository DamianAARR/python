#Inicializar listas y variables
datos_personales = []
alumnos = []
listaNotasMedias = []
notasIndividualesStr = []
notasIndividualesNum = []
dniAlumnos = []
notaMedia = 0
dato = ''

#---Parte 1 Ejercicio---
#SIN COMPLETAR
base_datos = [['Miguel', 'Rodriguez', '12311267A', '23424', '4', '2.1', '4.6', '3.4']]
mensaje = 'David Fernandez 12311267A 43527 2 2.1 4.6 3.4'
datos_alumno = mensaje.split()
base_datos.append(datos_alumno)
print(base_datos)

#---Parte 2 Ejercicio---
mensaje = 'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\nMaria Garcia 12316487A 43527 2 7.1 8.6 5.4\nJuan Perez 647829236A 43527 2 8.1 8.5 8.4\n'
'''David  Fernandez  12311267A   43527  2  9.1  7.6  2.4\n
   Maria  Garcia     12316487A   43527  2  7.1  8.6  5.4\n
   Juan   Perez      647829236A  43527  2  8.1  8.5  8.4\n'''

#Recorrer el string caracter a caracter
#Se podría separar también con el método split --> mensaje.split('\n')
for i in range(0,len(mensaje)):
    if mensaje[i] == ' ':
        datos_personales.append(dato)
        dato = ''
    elif mensaje[i] == '\n':
        datos_personales.append(dato)
        dato = ''
        alumnos.append(datos_personales)
        datos_personales = []
    else:
        dato = dato + mensaje[i]

#Recorrer la lista alumnos y guardar en otra lista las notas 
for i in range(0,len(alumnos)):
    #Añadimos solo las posiciones '[5:8]' de cada sublista que es donde se encuentras las notas
    notasIndividualesStr.append(alumnos[i][5:8])

#Recorremos la nueva lista que solo contiene las notas
for i in range(0,len(notasIndividualesStr)):
    for j in range(0,len(notasIndividualesStr)):
        #Convertimos cada elemento de strign a float para poder operar con ellos
        notasIndividualesNum.append(float(notasIndividualesStr[i][j]))
    #Calculamos la nota media
    notaMedia = sum(notasIndividualesNum) / len(notasIndividualesNum)
    #Añadimos la nota media a una nueva lisat y guardamos solo dos decimales con el método round (6.366666666666666 --> 6.37)
    listaNotasMedias.append(round(notaMedia,2))
    #Vaciamos la lista para empezar de nuevo con el siguiente alumno
    notasIndividualesNum = []
    #Igual con la nota media
    notaMedia = 0

#Recorremos la lista alumnos de nuevo ahora para sacar los DNIs
for i in range(0,len(alumnos)):
    #Guardamos en una lista nueva solo los DNIs que se encuentran en la posición '[i][2]' ([0][2],[1][2],[2][2])
    dniAlumnos.append(alumnos[i][2])

#Devolvemos el resultado por pantalla
for i in range(0,len(alumnos)):
    #Imprimimos el DNI y la nota media de cada alumno
    print('DNI:',dniAlumnos[i],'Nota Media:',listaNotasMedias[i])