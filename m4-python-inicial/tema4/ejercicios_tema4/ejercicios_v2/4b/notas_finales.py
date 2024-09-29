import numpy as np

calificaciones = np.array([
    [5,8,2,9],
    [3,2,7,7],
    [6,8,7,5],
    [6,8,7,5]
])

# extraer categoría de notas
examen1 = calificaciones[:,0]
examen2 = calificaciones[:,1]
trabajo_final = calificaciones[:,2]
participacion = calificaciones[:,3]

# calcular las notas y almacenarlas en un array nuevo
notas_finales = examen1 * 0.3 + examen2 * 0.3 + trabajo_final * 0.3 + participacion * 0.1

# devolver las notas
for nota in notas_finales:
    print(nota.round(2))