import numpy as np

red_social = [
    ("Juan",  ["Maria", "Pedro", "Luis"]),
    ("Maria", ["Juan",  "Pedro", "Juan"]),
    ("Pedro", ["Juan",  "Maria"]),
    ("Luis",  ["Juan"])]

new_red_social = []
num_amigos = []
users = []

#Eliminar las cuentas duplicadas de amigos
for tupla in red_social:
    usuario, amigos = tupla
    users.append(usuario)
    amigos = tuple(set(amigos))
    tupla = usuario, len(amigos)
    num_amigos.append(len(amigos))
    new_red_social.append(tupla)

print()
print(tuple(new_red_social))
print()

#Usuario con más amigos
num_amigos_ascendente = np.argsort(num_amigos)
print('Usuario con más amigos:',users[num_amigos_ascendente[-1]])
print()



