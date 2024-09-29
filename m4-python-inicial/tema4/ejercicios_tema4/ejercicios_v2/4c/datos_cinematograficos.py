import numpy as np

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

# género de película más popular, cuántas películas
# se lanzaron en cada década y cuál es la duración
# promedio de cada género de película

# extraer los géneros
generos, conteos = np.unique(peliculas[:,1], return_counts=True)
# ordenar índices en orden ascendente
conteos_ascendente = np.argsort(conteos)
# filtrar por el índice último que significa que es el que más se repite [3 4 3] --> [0 2 1]
genero_popular = generos[conteos_ascendente[-1]]
print(genero_popular)
# extraer las décadas
decadas = np.unique(peliculas[:,3].astype(int) // 10 * 10) #floor_divide
conteos_decadas = []
print()
for decada in decadas:
   conteo = np.count_nonzero((peliculas[:,3].astype(int) >= decada) & (peliculas[:,3].astype(int) < decada + 10))
   print('En la decada',decada,'se lanzaron',conteo,'peliculas')
# duracion promedio de cada género 
todos_generos = np.array(peliculas[:,1])

print()
for i in range(0,len(generos)):
    duracion_media = np.mean(peliculas[:,2].astype(float)[todos_generos == generos[i]])
    print('Duración media de',generos[i],':',duracion_media.round(2),'minutos')


