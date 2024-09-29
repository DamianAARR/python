import numpy as np
# array con datos de peliculas

se_repite = 0
genero_popular = ''
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

#años = peliculas[:,3]
calificaciones = peliculas[:,4]

# 1.- género más popular

# obtener generos y apariciones en la base de datos
generos, conteos = np.unique(peliculas[:,1], return_counts=True)
print(generos)
print(conteos)
print('----------')

#ordenar los conteos de mayor a menor 
conteos_desc = np.argsort(conteos)[::-1] #Nos devuelve los indices de los elementos de 'conteos'
                                         #ordenados de mayor a menor.
print(conteos_desc)
print('---------')
# extraer el género más popular
genero_popular = generos[conteos_desc[0]] #es decir, is igual a genero que más se repite y como hemos ordenado
                                          #los índices de mayor a menor ([3,4,3] --> Índices:[1,2,0]),
                                          # el que más se repite está en la posición [0].
print('Género más popular:', genero_popular)

# 2.- películas lanzadas en cada década

# creamos array con las décadas a tratar
decadas = np.unique(peliculas[:,3].astype(int) // 10 * 10)

# hacemos un conteo de las películas lanzadas en cada década
conteos_decadas = []

for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int) >= decada) & (peliculas[:,3].astype(int) < decada + 10))
    conteos_decadas.append(conteo)
    print('En la década',decada,'se lanzaron',conteo,'películas')

# 3.- duración media de cada género

todos_generos = peliculas[:,1]
duraciones = peliculas[:,2]
duracion_media = np.zeros(len(generos)) #len(generos) porque hay que almacenar la duración de cada película

#calcular la duracion media
for i in range(0,len(generos)):
    duracion_media[i] = np.mean(duraciones[todos_generos == generos[i]].astype(float)) #d_m[i] es igual a la media de las duraciones
                                                                                       #del género que estamos tratando 'generos[i]'
                                                                                       #en la lista de todos los generos 'todos_generos'
    print(generos[i])
    print(duracion_media[i].round(2))