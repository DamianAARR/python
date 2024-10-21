import numpy as np

# Funciones
def check_genero_mayor_calif(pelis):
    # Comprueba el género más popular
    generos = np.array(pelis[:,1])
    generos_unicos = np.unique(generos)
    califs = np.array(pelis[:,4].astype(float))
    califs_medias = np.zeros(len(generos_unicos))

    for i in range(0,len(generos_unicos)):
        califs_medias[i] = np.mean(califs[generos == generos_unicos[i]])
    
    califs_medias_ord = np.argsort(califs_medias)
    gen_mayor = generos_unicos[califs_medias_ord[-1]]
    calif_mayor = califs_medias[califs_medias_ord[-1]]
    return gen_mayor, calif_mayor

    
def check_genero_pop(pelis):
   # Comprueba el género más popular
    generos = np.array(pelis[:,1])
    generos_unicos, conteos = np.unique(generos, return_counts=True)
    conteos_ord = np.argsort(conteos)
    
    gen_pop = generos_unicos[conteos_ord[-1]]
    return gen_pop


def check_duracion_gen(pelis):
    generos = np.array(pelis[:,1])
    generos_unicos = np.unique(generos)
    duraciones = np.array(pelis[:,2].astype(int))
    duraciones_medias = np.zeros(len(generos_unicos))
    
    for i in range(len(generos_unicos)):
        duraciones_medias[i] = np.mean(duraciones[generos == generos_unicos[i]])
        print('Género:',generos_unicos[i],'- Duración media:',duraciones_medias[i].round(1))


# Caso de uso
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

# Género con más puntuación
genero, puntuacion = check_genero_mayor_calif(peliculas)

print('Género con la mayor calificación media:', genero, '-',puntuacion)
print()
# Género más popular
gen_pop = check_genero_pop(peliculas)
print('Género más popular:', gen_pop)
print()

# Películas lanzadas en cada década


# Duración promedio de cada género
check_duracion_gen(peliculas)
