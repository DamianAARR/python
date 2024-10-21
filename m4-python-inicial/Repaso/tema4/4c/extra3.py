import numpy as np

##### FUNCIONES #####
def dias_lluvia(clima):
    #Comprueba cuantos días en total llovió
    dias_lluvia = np.sum(clima[:,3].astype(int))
    return dias_lluvia


def temp_min_alta(clima):
    #Comprueba cuál es la ciudad con la temp min más alta
    ciudades = np.array(clima[:,0])
    temps_min = np.array(clima[:,2])
    temps_min_ord = np.argsort(temps_min)

    ciudad = ciudades[temps_min_ord[-1]]
    return ciudad


def temp_media_meses(clima):
    #Calcula la media de temperaturas por meses
    meses = np.array(clima[:,4])
    meses_unicos = np.unique(meses)
    temps = np.array([[int(elemento[i]) for i in range(1,3)]for elemento in clima])
    medias = np.zeros(len(meses_unicos))

    for i in range(0,len(medias)):
        medias[i] = np.mean(temps[meses == meses_unicos[i]])
        print('Mes:',meses_unicos[i],'-Temp promedio:',medias[i].round(1))


##### CASO DE USO #####

clima = np.array([
# Ciudad     T_Max T_Min Prec    Mes
['Ciudad A',   30,   20,  0,    'Enero'],
['Ciudad B',   28,   22,  5,    'Enero'],
['Ciudad C',   25,   15,  10,   'Febrero'],
['Ciudad A',   29,   19,  0,    'Enero'],
['Ciudad B',   31,   21,  0,    'Febrero'],
['Ciudad C',   27,   16,  3,    'Enero']
])


# 1.- Días totales con lluvia
dias = dias_lluvia(clima)
print('En total llovió,',dias,'días')
print()

# 2.- Ciudad con la temperatura mínima más alta
ciudad = temp_min_alta(clima)
print('Ciudad con la Temp Min más alta:',ciudad)
print()

# 3.- Temperatura promedio por meses
temp_media_meses(clima)