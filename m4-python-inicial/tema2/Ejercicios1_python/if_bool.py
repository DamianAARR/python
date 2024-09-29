
#Preguntar por pantalla si ha pagado o no
respuesta = input('Has pagado?').strip().lower()


#Convertir respuesta en booleano
if respuesta in "si":
    haPagado = True
elif respuesta in "no":
    haPagado = False
else:
    print('Respuesta no válida')


#Comprobar si ha pagado o no
if haPagado == False:
    print('Aun no has pagado')
    precio = float(input('Cuál es el precio?'))
    if precio <= 20:
        print('Tienes que pagar menos de 20 euros')
    else:
        print('Tienes que pagar más de 20 euros')
elif haPagado == True:
    print('Ya has pagado')    
else:
    print('Respuesta inválida')
