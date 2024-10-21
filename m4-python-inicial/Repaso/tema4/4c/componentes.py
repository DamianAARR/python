import numpy as np

##### FUNCIONES #####
def comp_mayor_punt(datos):
    # Comprueba el componente con mayor puntuación
    componentes = np.array(datos[:,1])
    puntuaciones = np.array(datos[:,3])
    punt_ord = np.argsort(puntuaciones)
    componenete = componentes[punt_ord[-1]]
    return componenete


def comp_meses(datos):
    # Comprueba cuantos componentes se produjeron cada mes
    fechas = np.array(datos[:,0])
    meses = list(int(fecha[5:7]) for fecha in fechas)
    meses_unicos, conteos = np.unique(meses, return_counts=True)
    comp_por_mes = np.zeros(len(meses_unicos))

    for i in range(0,len(comp_por_mes)):
        comp_por_mes[i] = conteos[i]
        print('Mes:',i+1,'-',conteos[i],'componentes')
    print()

def punt_promedio(datos):
    # Comprueba la puntuacion promedio de cada componenete
    componentes = np.array(datos[:,1])
    puntuaciones = np.array(datos[:,3].astype(int))
    componentes_unicos = np.unique(componentes)

    medias_comp = np.zeros(len(componentes_unicos))

    for i in range(len(medias_comp)):
        medias_comp[i] = np.mean(puntuaciones[componentes == componentes_unicos[i]])
        print('Componenete:',i+1,'- Puntuación promedio:',medias_comp[i].round(1))

##### CASO DE USO #####

# Datos almacenados en array
datos = np.array([
#      FECHA            TIPO         LOTE   PUNT
    ['2022-01-01', 'Componente 1', 'Lote A', 80],
    ['2022-01-15', 'Componente 1', 'Lote B', 90],
    ['2022-02-01', 'Componente 2', 'Lote C', 85],
    ['2022-02-15', 'Componente 2', 'Lote D', 95],
    ['2022-03-01', 'Componente 1', 'Lote E', 75],
    ['2022-04-01', 'Componente 1', 'Lote E', 75],
    ['2022-04-01', 'Componente 1', 'Lote E', 75],
    ['2022-04-01', 'Componente 1', 'Lote E', 75],
    ['2022-05-01', 'Componente 1', 'Lote E', 75],
    ['2022-05-01', 'Componente 1', 'Lote E', 75],
    ['2022-05-01', 'Componente 1', 'Lote E', 75],
    ['2022-05-01', 'Componente 1', 'Lote E', 75],
    ['2022-05-01', 'Componente 1', 'Lote E', 75],
    ['2022-05-01', 'Componente 1', 'Lote E', 75],
    ['2022-03-15', 'Componente 2', 'Lote F', 90]
])

# 1.- Componente con la puntuación más alta
comp_mayor_puntuacion = comp_mayor_punt(datos)
print('Componente con la puntuación más alta:',comp_mayor_puntuacion[-1])
print()

# 2.- Componentes producidos en cada mes

comp_meses(datos)


# 3.- Puntuacion promedio de cada tipo de componente
punt_promedio(datos)
