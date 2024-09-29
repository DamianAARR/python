#Inicializar listas y variables
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

nuevo_caracter = ''
palabra_codificada = ''

#Pedir una palabra por consola
palabra = input('Introduce una palabra: ')
palabra2 = input('Introduce la codificacion ROT13 de la palabra anterior: ')

#Recorrer cada letra de la palabra introducida
for letra in palabra:
    #Comprobamos si es minúscula o mayúscula
    if letra.islower():
        #Comprobamos el índice de cada letra y le sumamos 12 (en total hace 13) y lo guardamos en una nueva variable
        nuevo_caracter = abecedario.index(letra) + 13
        #Multiplicamos la lista del abecedario por dos para que vuelva a empezar de nuevo si el índide es mayor a 26
        caracteres = abecedario * 2
        #Guardamos cada nuevo caracter en una nueva variable concatenando con el valor anterior
        palabra_codificada = palabra_codificada + caracteres[nuevo_caracter].lower()
        #Reseteamos el valor de la variable para pasar almacenar el índice de la siguiente letra
        nuevo_caracter = ''
    #Comprobamos si es minúscula o mayúscula    
    if letra.isupper():
        #Añadimos el método .lower() para no necesitar tener dos listas de abecedario
        nuevo_caracter = abecedario.index(letra.lower()) + 13
        caracteres = abecedario * 2
        #Como la letra introducida es mayúscula añadimos el método .upper() para guardar el nuevo caracter en mayúscula
        palabra_codificada = palabra_codificada + caracteres[nuevo_caracter].upper()
        nuevo_caracter = ''

#Comprobamos si la palabra introducida como ROT13 es correcta o no
if palabra2 == palabra_codificada:
    print()
    print('Correcto,',palabra2,'es la codificación ROT13 de',palabra)
else:
    print()
    print('La codificacion ROT13 no coincide. Es:',palabra_codificada)


