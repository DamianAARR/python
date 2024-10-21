import numpy as np

#FUNCIONES
def calcular_medias(clima):
    # Calcula la media de temperaturas
    temperatura = clima[:,0]
    humedad = clima[:,1]
    precipitacion = clima[:,2]
    meses = clima[:,3]
    # Listas finales
    temp_media_meses = []
    hum_media_meses = []
    prec_media_meses = []

    for i in range(0,12):
        temps = []
        hum = []
        prec = []
        temps.append(temperatura[meses == i])
        media = np.mean(temps)
        temp_media_meses.append(media)
        media = []
        hum.append(humedad[meses == i])
        media = np.mean(hum)
        hum_media_meses.append(media)
        media = []
        prec.append(precipitacion[meses == i])
        media = np.mean(prec)
        prec_media_meses.append(media)
        media = []

    return temp_media_meses, hum_media_meses, prec_media_meses


def imprimir_resultados(temp,hum,prec):
    #Devuelve los resultados obtenidos
    for i in range(0,12):
        print('Mes',i + 1,'T media:',temp[i].round(1),'H media:',hum[i].round(1),'P media:',prec[i])


def calcular_medias2(clima):
    meses = clima[:,3]

    temp_media = np.zeros(12)
    hum_media = np.zeros(12)
    prec_media = np.zeros(12)

    for i in range(0,12):
        mediciones = clima[meses == i]
        temp_media[i] = np.mean(mediciones[:,0])
        hum_media[i] = np.mean(mediciones[:,1])
        prec_media[i] = np.mean(mediciones[:,2])

    return temp_media,hum_media,prec_media



#CASO DE USO
clima = np.array([
#    T   H    P    M
    [20, 70, 1009, 1],
    [21, 60, 1011, 1],
    [22, 40, 1010, 1],
    [18, 75, 1012, 2],
    [21, 60, 1008, 3],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [27, 49, 1007, 5],
    [29, 50, 1007, 5],
    [28, 51, 1007, 5],
    [30, 45, 1005, 6],
    [10, 30, 1005, 6],
    [32, 40, 1002, 7],
    [33, 35, 1001, 8],
    [31, 45, 1003, 9],
    [30, 42, 1001, 9],
    [29, 42, 1002, 9],
    [35, 43, 1001, 9],
    [28, 50, 1006, 10],
    [25, 60, 1010, 11],
    [27, 59, 1012, 11],
    [24, 58, 1011, 11],
    [22, 70, 1011, 12]
])

#llamar a la función que calcula la media de temperatura
#temp_media, hum_media, prec_media = calcular_medias(clima)

#Llamar funcion v2
temp, hum, prec = calcular_medias2(clima)

#llamar a la función que devuelve los resultados
imprimir_resultados(temp,hum,prec)


