import numpy as np

#Datos de ventas de la tienda
ventas = np.array([
    ['2022-01-01',100,'ropa'],
    ['2022-01-02',200,'alimentos'],
    ['2022-01-03',150,'ropa'],
    ['2022-02-01',120,'alimentos'],
    ['2022-02-02',180,'electronicos'],
    ['2022-02-03',200,'alimentos'],
    ['2022-03-01',90,'ropa'],
    ['2022-03-02',110,'electronicos'],
    ['2022-03-03',100,'alimentos']
])

# extraer los meses y montos
fechas = np.array([venta[0] for venta in ventas])

meses = np.array([int(fecha[5:7])for fecha in fechas])
print('meses:')
print(meses)

# filtrar las ventas por mes y almacenarlas en un nuevo array
montos_mes = np.zeros(12)

for i in range(1,13):
    ventas_mes = ventas[meses == i]
    montos_mes[i-1] = np.sum(ventas_mes[:,1].astype(int))
print(montos_mes)