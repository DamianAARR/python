
respuesta = input('Has pagado? | si o no')

if respuesta == 'no':
    print('Aun no has pagado')
    precio = float(input('Cuál es el precio?'))
    if precio <= 20:
        print('Tienes que pagar menos de 20 euros')
    else:
        print('Tienes que pagar más de 20 euros')
elif respuesta == 'si':
    print('Ya has pagado')    
else:
    print('Respuesta inválida')

# if hasPagado == False:
#     print('Aun no has pagado')
#     precio = float(input('Cuál es el precio?'))
#     if precio <= 20:
#         print('Tienes que pagar menos de 20 euros')
#     else:
#         print('Tienes que pagar más de 20 euros')
# else:
#     print('Ya has pagado')
