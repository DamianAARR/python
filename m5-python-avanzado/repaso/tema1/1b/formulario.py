##### FUNCIONES #####
def validar_formulario(name,email,tlf):
    if (len(name) > 3) and ('@' in email) and ('.' in email) and tlf.isnumeric() and (len(tlf) == 9):
        print(True)
    else:
        print('Algún dato no cumple los requisitos')


##### CASO DE USO #####
nombre = input('Introduce tu nombre: ')
email = input('Introduce tu email: ')
tlf = input('Introduce tu número: ')

validar_formulario(nombre,email,tlf)