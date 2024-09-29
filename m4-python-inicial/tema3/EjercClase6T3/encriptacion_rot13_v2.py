#Inicializar listas y variables
#abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abecedario = 'abcdefghijklmnopqrstuvwxyz'
abecedario_mayus = abecedario.upper()
indice_letra = 0
nuevo_indice = 0
palabra_codificada = ''
letra_nueva = ''

#Pedir una palabra por consola
palabra = input('Introduce una palabra: ')
#palabra2 = input('Introduce la codificacion ROT13 de la palabra anterior: ')

#Recorrer cada letra de la palabra introducida
for letra in palabra:
    #Comprobamos si es minúscula
    if letra in abecedario:
        #Recorremos el abecedario
        for i in range(len(abecedario)):
            #Cuando encuentre la letra en el abecedario guardamos el índice
            if letra == abecedario[i]:
                indice_letra = i
                #Si el índice +13 es >= 26 restamos 26 para que vuelva al principo
                if indice_letra + 13 >= 26:
                    indice_letra = indice_letra - 26

                nuevo_indice = indice_letra + 13
                letra_nueva = abecedario[nuevo_indice]

    elif letra in abecedario_mayus:
         #Recorremos el abecedario
        for i in range(len(abecedario_mayus)):
            #Cuando encuentre la letra en el abecedario guardamos el índice
            if letra == abecedario_mayus[i]:
                indice_letra = i
                #Si el índice +13 es >= 26 restamos 26 para que vuelva al principo
                if indice_letra + 13 >= 26:
                    indice_letra = indice_letra - 26

                nuevo_indice = indice_letra + 13
                letra_nueva = abecedario_mayus[nuevo_indice]    
                   
    palabra_codificada = palabra_codificada + letra_nueva
  
print(palabra_codificada)



