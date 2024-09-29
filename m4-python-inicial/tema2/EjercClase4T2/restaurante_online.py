#Pedir por pantalla que tipo de hamburguesa quiere
burger = input('Qué hamburguesa quieres? --> ')

#Mostrar los ingredientes extra en función de la hamburguesa que ha escogido
if burger.lower() == 'clasica':
    extraC = input('Elige un ingrediente extra: \nQueso idiazabal\nBacon\nHuevo\n')
    print('Has elegido la hamburguesa',burger.title(),'con',extraC.title())
elif burger.lower() == 'vegana':
    extraV = input('Elige un ingrediente extra: \nTofu\nCebolla carmelizada\n')
    print('Has elegido la hamburguesa',burger.title(),'con',extraV.title())
else:
    print('Ese tipo de hamburguesa no está disponible ')