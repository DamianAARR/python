
datos = {'damian': 140, 'pepe': 150}

votos_totales = 0
for votos in datos.values():
    votos_totales += votos

for clave, valor in datos.items():
    porcentaje = valor * 100 / votos_totales
    print(clave.title(),':',porcentaje.round(1),'%')
