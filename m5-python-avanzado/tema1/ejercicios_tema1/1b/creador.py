# ----MÓDULOS----
import random as rd
import string as st

# ----FUNCIONES----
def generar_contrasena():
    #Genera una contraseña nueva de forma aleatoria
    print('---- Generador de contraseñas ----')
    longitud_user = int(input('Longitud de la contraseña:\n'))
    add_mayus = input('Introducir mayúsculas? (si o no)\n')
    add_minus = input('Introducir minúsculas? (si o no)\n')
    add_nums = input('Introducir números? (si o no)\n')
    add_car = input('Introducir caractéres especiales? (si o no)\n')

    todos_caracteres = ''

    if add_mayus == 'si':
        todos_caracteres += st.ascii_uppercase
        
    if add_minus == 'si':
        todos_caracteres += st.ascii_lowercase
    
    if add_nums == 'si':
        todos_caracteres += st.digits
        
    if add_car == 'si':
        todos_caracteres += st.punctuation
        

    pass_generada = '' .join(rd.choice(todos_caracteres) for i in range(longitud_user))

    return pass_generada
        



