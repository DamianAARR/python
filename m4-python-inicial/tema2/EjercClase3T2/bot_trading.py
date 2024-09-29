#Pedir un precio por consola
precio = float(input('Introduce el precio: '))

#Comprobar si se debe comprar, holdear o vender
if precio < 100:
    print()
    print('BOT: Es momento de comprar.')
    print()
elif precio >= 100 and precio <= 150: #Podría ser: elif 100.0 <= precio <= 150.0:
    print()
    print('BOT: De momento vamos a holdear.')
    print()
elif precio > 150:
    print()
    print('BOT: Es momento de vender.')
    print()
