#Crear dos listas
nombres = ['damian','nayra','mama','carlillos','antonio','lucia','paul']
nombres2 = ['damian','nayra','juan','manolo','pepe','paquillo','manuela','jorge','luis','mama']
comunes = []

mio = 'damian'

#Comprobar elementos comunes y añadir a otra lista

for i in range(0,len(nombres)):
    for j in range(0,len(nombres2)):
        if nombres[i] == nombres2[j]:
            comunes.append(nombres[i])

#VERSIÓN PROFE
for elemento in nombres:
    if elemento in nombres2:
        comunes.append(elemento)

#Devolver respuesta
print('Elementos comunes:',*comunes)



