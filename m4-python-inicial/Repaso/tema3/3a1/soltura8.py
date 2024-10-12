#FUNCIONES 
def comprobar_apariciones(num_user):
    # Comprueba el número de apariciones
    lista = [2,4,6,2,7,8,4,5,6,3,8,9,2,3,4,4,5,4,3,7,3,5,6,3,2,4,6,7,4,2,3,5,7,8,9,6,34,]
    num_apariciones = lista.count(num_user)
    return num_apariciones


def imprimir_mensaje(num,apariciones):
    # Imprime el mensaje final
    print('El número',num,'aparece',apariciones,'veces en la lista.')

    
#Caso de uso
num_user = int(input('Introduce un número entero: \n'))

#Llamar a la función que comprueba el número de apariciones
apariciones = comprobar_apariciones(num_user)

#Llamar a la función que imprime el mensaje
imprimir_mensaje(num_user,apariciones)