#Paso 1
print('Paso 1')
my_tupla = (1,'hola',True)
print(my_tupla[0])
print(my_tupla[1])
print(my_tupla[2])
print()

#Paso 2
print('Paso 2')
my_lista = [1,2,3]
my_lista[1] = 0
# my_tupla[1] = 0 --> ERROR: no se pueden modificar los elementos
print(my_lista)
print()

#Paso 3
print('Paso 3')
tupla_enteros = (1,2,3,4,5,6,7,8,9)
suma_tupla = sum(tupla_enteros)
print(suma_tupla)
print()

#Paso 4
print('Paso 4')
tupla_strings = ('hola','mundo','hello','world')
lista_caract = []

for tupla in tupla_strings:
    lista_caract.append(tupla[0])
        
tupla_caract = tuple(lista_caract)
print(tupla_strings)
print(tupla_caract)
print()

#Paso 5
print('Paso 5')
pares = []
producto = 1
for entero in tupla_enteros:
    if entero & 2 == 0:
        pares.append(entero)

for par in pares:
    producto *= par
print('Pares:',pares)
print('Producto:',producto)
print()

#Paso 6
print('Paso 6')
numbers = (2,6,3,9,1,7,5,8,4)
numbers_ord = tuple(sorted(numbers))
print('Tupla:',numbers)
print(type(numbers))
print('Tupla ordenada:', numbers_ord)
print(type(numbers_ord))
print()

#Paso 7
print('Paso 7')
nums = (1,1,2,2,3,3,4,4,5,5)
nums_unicos = set(nums)
print('Tupla:',nums)
print('Numeros únicos:',nums_unicos)
print()

#Paso 8
print('Paso 8')
num_int = 45
print(num_int in tupla_enteros)

#Paso 9
print('Paso 9')
tupla1 = (1,2,3,4,5,6)
tupla2 = ('d','a','m','i','a','n')
tupla_unida = tuple(zip(tupla1,tupla2))
print(tupla1)
print(tupla2)
print(tupla_unida)
print()

#Paso 10
print('Paso 10')
minimo = min(tupla_enteros)
maximo = max(tupla_enteros)
print('Min:',minimo)
print('Max:',maximo)
print()

#Paso 11
print('Paso 11')
apellidos = ('lopez','dehn','rodriguez')
corto = min(apellidos, key=len)
largo = max(apellidos, key=len)
print(corto)
print(largo)
print()

#Paso 12
print('Paso 12')
tupla_invertida = tuple(reversed(tupla_enteros))
print(tupla_enteros)
print(tupla_invertida)
print()

#Paso 13
print('Paso 13')
tupla_tuplas = ((1,2),(3,4),(5,6),(7,8),(9,10))
sumas = []

for tupla in tupla_tuplas:
    suma = 0
    suma = sum(tupla)
    sumas.append(suma)

tupla_sumas = tuple(sumas)
print(tupla_sumas)