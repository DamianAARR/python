import numpy as np


arr = np.array([2010, 1995, 1875, 1987])
flor_division = arr // 10 * 10
print(flor_division)

quit()
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

generos = np.array([peliculas[:,1]])

unicos, conteos = np.unique(generos, return_counts=True)
print(unicos)
print(conteos)