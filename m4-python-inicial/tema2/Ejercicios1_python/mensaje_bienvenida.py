#Pedir el nombre por consola
print('Cuál es tu nombre?')
nombre = input()

#Almacenar el mensaje con el valor introducido
mensaje_bienvenida = 'Hola, ' + nombre.replace(".","").title() + '! Estás usando Python'

#Imprimir el mensaje completo
print(mensaje_bienvenida)