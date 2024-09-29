#Crear una lista

nombres = ['damian','nayra', 'damian', 'celia','mama','david','lucas','celia']
repetidos = []
unicos = []
#Encontrar elementos duplicados de la lista y añadirlos a una nueva lista
for i in range(0,len(nombres)):
    for j in range(i + 1,len(nombres)):
        if nombres[i] == nombres[j]:
            repetidos.append(nombres[i])

#Versión profe
for elemento in nombres:
    if nombres.count(elemento) > 1:
        if elemento not in repetidos:
            repetidos.append(elemento)
    else:
        unicos.append(elemento)

#Borrarlos de la lista
for nombre in repetidos:
    nombres.remove(nombre)

for elemento in repetidos:
    nombres.remove(elemento)

#Imprimir lista con elementos únicos
print(nombres)
print(repetidos)

