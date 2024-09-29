#Pedir por pantalla si es chico o chica y el nombre
genero = input('Eres chico o chica?')
nombre = input('Cuál es tu nombre?')
chica_grupoA = ('e','f','g','h','i','j','l','m')
chico_grupoA = ('a','b','c','d','e','f','g','h','r','s','t','u','v','w','x','y','z')

#Comprobar a qué grupo pertenece cada nombre y mostrarlo por pantalla
# if genero.lower() == 'chica' and nombre.lower().startswith(chica_grupoA):
#     print('La alumna',nombre.title(),'pertenece al grupo A')
# elif genero.lower() == 'chica':
#     print('La alumna',nombre.title(),'pertenece al grupo B')
# elif genero.lower() == 'chico' and nombre.lower().startswith(chico_grupoA):
#     print('El alumno',nombre.title(),'pertenece al grupo A')
# else:
#     print('El alumno',nombre.title(),'pertenece al grupo B')


#VERSIÓN PROFE

nombres_chicasA = 'EFGHIJLM'
nombres_chicosA = 'ABCDEFGHRSTUVWXYZ'

if genero.lower() == 'chica':
    if nombre[0].upper() in nombres_chicasA:
        print('La alumna',nombre.title(),'pertenece al grupo A')
    else:
        print('La alumna',nombre.title(),'pertenece al grupo B')
elif genero.lower() == 'chico':
    if nombre[0].upper() in nombres_chicosA:
        print('El alumno',nombre.title(),'pertenece al grupo A')
    else:
        print('El alumno',nombre.title(),'pertenece al grupo B')
else:
    print('Error: Reinicia el programa e introduce un género válido.')