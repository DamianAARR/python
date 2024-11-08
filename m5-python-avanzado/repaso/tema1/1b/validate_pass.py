##### MÓDULOS #####
from generate_pass import gen_pass
import string as st
import random as rd


##### FUNCIONES #####
def validar_pass(user_pass):
    #Comprueba si la password introducida cumple los requisitos
    mayus = st.ascii_uppercase
    minus = st.ascii_lowercase
    nums = st.digits
    signos = st.punctuation
    
    if (len(user_pass) >= 8) and any(letra in mayus for letra in user_pass) and any(letra in minus for letra in user_pass) and any(num in nums for num in user_pass)and any(signo in signos for signo in user_pass):
        print()
        print('Contraseña validada correctamente')
    else:
        print('Invalid password')
        new_pass = gen_pass()
        print()
        print('New password generated:',new_pass)


##### CASO DE USO #####
user_pass = input('Introduce tu contraseña:\n')

#Llamar a la función que lo comprueba
validar_pass(user_pass)