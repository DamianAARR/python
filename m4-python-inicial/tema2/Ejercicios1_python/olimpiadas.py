#Pedir por pantalla los tiempor en minutos, segundos y centésimas
print('Introduzca su nombre')
nombre = input()
print('Introduzca los minutos')
minutos = int(input())
print('Introduzca los segundos')
segundos = int(input())
print('Introduzca las centésimas')
centesimas = int(input())

#Convertir los tiempos a segundos
minutos_Segundos = minutos * 60
centesimas_Segundos = float(centesimas / 100) 
total_segundos = minutos_Segundos + segundos + centesimas_Segundos

#Calcular velocidad media
metros_pista = 100
velocidad_media_segundos = total_segundos / metros_pista

#Imprimir los resultados por pantalla
#print('La velocidad media de ', nombre, ' es de ', velocidad_media_segundos, 'segundos por metro')

print('La velocidad media de ', nombre, ' es de 1 metro cada', velocidad_media_segundos, 'segundos')