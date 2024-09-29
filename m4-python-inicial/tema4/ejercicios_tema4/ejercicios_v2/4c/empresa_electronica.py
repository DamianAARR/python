import numpy as np

# Crear un array con los datos
datos = np.array([
    #   FECHA           TIPO         LOTE     PUNT
    ['2022-01-01', 'Componente 1', 'Lote A',   80],
    ['2022-01-15', 'Componente 1', 'Lote B',   90],
    ['2022-02-01', 'Componente 2', 'Lote C',   85],
    ['2022-02-15', 'Componente 2', 'Lote D',   95],
    ['2022-03-01', 'Componente 1', 'Lote E',   75],
    ['2022-03-15', 'Componente 2', 'Lote F',   90]
    ])

# cuál es el tipo de componente con la puntuación de calidad más alta, 
# cuántos componentes se produjeron en cada mes y
# cuál es la puntuación de calidad promedio de cada tipo de componente.

#extraer componentes
componentes = np.array([dato[1] for dato in datos])

# extraer puntuaciones 
puntuaciones = np.array([dato[3] for dato in datos])

# extraer el índice del elemento más grande
indice_mayor = np.argmax(puntuaciones)
mayor_puntuacion = puntuaciones[indice_mayor]

mejor_componente = componentes[puntuaciones == mayor_puntuacion]
print()
print('Componente con mayor puntuación:',mejor_componente)

# extraer fechas
fechas = np.array([dato[0] for dato in datos])

meses = np.array([int(fecha[5:7]) for fecha in fechas])

print()
# contar cuantos componentes se fabricaron en cada mes
for i in range(1,13):
    comp_mes = np.count_nonzero([componentes[meses == i]])
    print('En el mes',i,'se produjeron:',comp_mes)

# for i in range(1,13):
comp_unicos = np.unique([dato[1] for dato in datos])
print()
for i in range(0,len(comp_unicos)):
    punt_media = np.mean(puntuaciones[componentes == comp_unicos[i]].astype(float)).round(2)
    print('Puntuación media del componente',*{i+1},':',punt_media)
