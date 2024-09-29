import numpy as np

calificaciones = np.array([
    [7, 5, 4, 5],
    [5, 8, 7, 9],
    [6, 7, 6, 8],
    [9, 5, 8, 9]
])

#Extraer calificaciones
examen1 = calificaciones[:,0]
examen2 = calificaciones[:,1]
trabajo_final = calificaciones[:,2]
participacion = calificaciones[:,3]

#Crear array con notas finales
notas_finales = examen1 * 0.3 + examen2 * 0.3 + trabajo_final * 0.3 + participacion * 0.10

#Devolver las notas finales con un bucle
for i in range(0,len(notas_finales)):
    print('La nota final del alumno' ,i+1, 'es:', notas_finales[i].round(1))

