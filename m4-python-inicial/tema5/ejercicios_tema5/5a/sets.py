#Paso 14
print('Paso 14')
mi_set = {1,2,3,4,5}
print(mi_set)
mi_set.discard(5)
print(mi_set)
print()

#Paso 15
print('Paso 15')
set_vacio = set()
print('Set vacío:', set_vacio)
print()

#Paso 16
print('Paso 16')
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9,1,2}
union = set1 | set2
interseccion = set1 & set2
diferencia = set1 - set2
print('Union:',union)
print('Inteseccion:',interseccion)
print('Diferencia:',diferencia)
print()

#Paso 17
print('Paso 17')
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9,1,2}
set_comunes = set1 & set2
print(set1)
print(set2)
print('Comunes:',set_comunes)
print()

#Paso 18
print('Paso 18')
set_enteros = {1,2,3,4,5,6,7,8,9}
minimo = min(set_enteros)
maximo = max(set_enteros)
print('Set:',set_enteros)
print('Mínimo:',minimo)
print('Máximo:',maximo)
print()

#Paso 19
print('Paso 19')
set_random1 = {1,4,15,23,65,25,12,5,9,42}
set_random2 = {56,87,23,9,90,4,54,15,12}
set_unicos = set_random1 ^ set_random2
print('Set 1:',set_random1)
print('Set 2:',set_random2)
print('Únicos:',set_unicos)
print()

#Paso 20
print('Paso 20')
colores = {'rojo','amarillo','azul','verde'}
color = 'morado'
if color in colores:
    print('True')
else:
    print('False')
print()

#Paso 21
print('Paso 21')
unicos_set1 = set1 - set2
print(set1)
print(set2)
print('Únicos set1:',unicos_set1)
print()

#Paso 22
print('Paso 22')
numbers = {1,2,3,4,5}
prod = 1
for number in numbers:
    prod *= number
print('Set:',numbers)
print('Producto de elementos:',prod)

