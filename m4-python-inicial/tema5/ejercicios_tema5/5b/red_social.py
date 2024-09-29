import numpy as np

#Base de datos red social
red_social = [
    ("Juan",  ["Maria", "Pedro", "Luis"]),
    ("Maria", ["Juan",  "Pedro", "Juan"]),
    ("Pedro", ["Juan",  "Maria"]),
    ("Luis",  ["Juan"])]

amigos_usuarios = []

#Convertir base de datos en lista para modificar elementos
for i in range(0,len(red_social)):
    red_social[i] = list(red_social[i])

#Extraer nombres de usuarios
usuarios = np.array([usuario[0] for usuario in red_social])

#Eliminar duplicados y convertir amigos en tupla
for usuario in red_social:
    usuario[1] = set(usuario[1])
    usuario[1] = tuple(usuario[1])
    #Guardar el número de amigos de cada usuario
    amigos_usuarios.append(len(usuario[1])) 

#Convertir usuarios en tupla
for i in range(len(red_social)):
    red_social[i] = tuple(red_social[i])
    
#Convertir base de datos en tupla
red_social = tuple(red_social)
print(red_social)
print()

#Usuario con más amigos
#convertir lista en array
amigos_array = np.array(amigos_usuarios)
#Ordenar indices de forma ascendente
amigos_ascendente = np.argsort(amigos_array)
#seleccionar el usuario con más amigos según el índice
user_mas_amigos = usuarios[amigos_ascendente[-1]]
numero_amigos = amigos_array[amigos_ascendente[-1]]

print('Usuario con más amigos:',user_mas_amigos,'-',numero_amigos,'amigos')


















