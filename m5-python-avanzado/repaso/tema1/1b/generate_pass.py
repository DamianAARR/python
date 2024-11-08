##### MÓDULOS #####
import random as rd
import string as st


##### FUNCIONES #####
def gen_pass():
    #Genera una nueva password aleatoria
    caracteres = ''
    new_pass = ''
    
    minus = input('Quieres usar minusculas? (si o no):\n')
    if minus == 'si':
        caracteres = st.ascii_lowercase
    
    mayus = input('Quieres usar mayúsculas? (si o no):\n')
    if mayus == 'si':
        caracteres += st.ascii_uppercase
    
    nums = input('Quieres usar números? (si o no):\n')
    if nums == 'si':
        caracteres += st.digits
    
    punt = input('Quieres usar signos de puntuación? (si o no):\n')
    if punt == 'si':
        caracteres += st.punctuation
    
    for i in range(0,9):
        caract = rd.choice(caracteres)
        new_pass += caract
    
    return new_pass