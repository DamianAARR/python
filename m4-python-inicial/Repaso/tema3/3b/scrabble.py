#FUNCIONES
def contar_puntos(mano):
    #Cuenta los puntos de la mano
    
    #for elemento in mano:
    #    puntos += int(elemento[-1])

    #Compresión del bloque anterior
    puntos = sum(int(elemento[-1]) for elemento in mano)
    
    return puntos


#CASO DE USO
mano = ['A3','T4','R1','E6','L7','I3','S2']

#Llamar a la función que cuente los puntos de la mano
puntos = contar_puntos(mano)

print('Puntos totales',puntos)