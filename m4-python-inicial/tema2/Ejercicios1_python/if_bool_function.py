
#Definir funcion que convierte la respuesta en booleano
def combrobar_respuesta(string):
    while True:
        respuesta = input(string + '| si o no').strip().lower()
        if respuesta in "si":
            return True
        elif respuesta in "no":
            return False
        else:
            print('Respuesta no válida')

#Llamar a la funcion que comprueba la respuesta
respuesta = combrobar_respuesta('Has pagado?')

#Comprobar si ha pagado o no
if respuesta == False:
    print('Aun no has pagado')
    precio = float(input('Cuál es el precio?'))
    if precio <= 20:
        print('Tienes que pagar menos de 20 euros')
    else:
        print('Tienes que pagar más de 20 euros')
elif respuesta == True:
    print('Ya has pagado')    
else:
    print('Respuesta inválida')
