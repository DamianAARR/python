#Pedir datos al usuario por pantalla
nombre = input('Introduce tu nombre: ')
edad = int(input('Introduce tu edad: '))
nota_media = float(input('Introduce tu nota media: '))

#Comprobar si cumple los requisitos y devolver respuesta por pantalla
if edad >= 17 and edad <= 21 and nota_media >= 8:
    print()
    print('Enhorabuena',nombre.title(),'tienes acceso a la beca!')
else:
    print()
    print('Lo sentimos,',nombre.title(),', no cumples los requisitos.')