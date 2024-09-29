import numpy as np
# array con datos de peliculas

se_repite = 0
genero_popular = []
decada_2000 = 0
decada_90 = 0
decada_80 = 0
decada_2010 = 0

pelisComedia = []
pelisAccion = []
pelisDrama = []

peliculas = np.array([
    #Título      Genero    Dura  Año    Cal
    ['Peli 1',  'Comedia', 120,  1990,  8.5],
    ['Peli 2',  'Acción',  110,  2005,  7.8],
    ['Peli 3',  'Drama',    95,  2010,  6.9],
    ['Peli 4',  'Comedia', 100,  1985,  7.5],
    ['Peli 5',  'Acción',  130,  2015,  8.1],
    ['Peli 6',  'Drama',   115,  2000,  6.7],
    ['Peli 7',  'Comedia',  90,  1995,  8.2],
    ['Peli 8',  'Acción',  105,  2010,  7.4],
    ['Peli 9',  'Drama',   125,  1980,  6.8],
    ['Peli 10', 'Comedia',  95,  2000,  8.0]
])

# extraer datos
titulo = peliculas[:,0]
genero = peliculas[:,1]
duracion = peliculas[:,2]
#años = peliculas[:,3]
calificaciones = peliculas[:,4]

# 1.- género más popular
for i in range(0,len(genero)):
    if np.count_nonzero(genero) > i:
        genero_popular = genero[i]

print('Género más popular:',genero_popular)
quit()
# 2.- películas lanzadas en cada década
años = np.array([pelicula[3] for pelicula in peliculas])
decadas = np.array([int(año[2]) for año in años])

for decada in decadas:
    if decada == 0:
        decada_2000 += 1
    elif decada == 9:
        decada_90 += 1
    elif decada == 8:
        decada_80 += 1
    else:
        decada_2010 += 1
print()
print('Películas lanzadas en cada década:')
print('1980:',decada_80,'\n1990:',decada_90,'\n2000:',decada_2000,'\n2010:',decada_2010)

# 3.- duración promedio de cada género
for pelicula in peliculas:
    for i in range(0,len(pelicula)):
        if pelicula[1] == 'Comedia':
            pelisComedia.append(int(pelicula[2]))
        if pelicula[1] == 'Acción':
            pelisAccion.append(int(pelicula[2]))
        if pelicula[1] == 'Drama':
            pelisDrama.append(int(pelicula[2]))
        break

promedioComedia = np.mean(pelisComedia)
promedioAccion = np.mean(pelisAccion)
promedioDrama = np.mean(pelisDrama).round(2)

print()
print('Duración promedio de cada género:')
print('Comedia:',promedioComedia,'\nAcción:',promedioAccion,'\nDrama:',promedioDrama)
