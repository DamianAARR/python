#PASO14
print('----------')
mi_set = {1,2,3,4,5}
mi_set.discard(3)
print(mi_set)

#PASO15
print('----------')
empty_set = set()
print(empty_set)

#PASO16
print('----------')
set1 = {1,2,3,4,5,6,7}
set2 = {6,7,8,9,10}

union = set1 | set2
print(union)

interseccion = set1 & set2
print(interseccion)

diferencia = set1 - set2
print(diferencia)

diferencia = set2 - set1
print(diferencia)


#PASO17
print('----------')
comunes = set1 & set2
print(comunes)


#PASO18
print('----------')
print('Máximo:',max(set1))
print('Mínimo:',min(set1))

#PASO19
print('----------')
unicos = set1 ^ set2
print(unicos)

#PASO20
print('----------')
colores = {'rojo','azul','amarillo','verde'}
comprobar = ('azul' in colores)
print(comprobar)

#PASO21
print('----------')
solo1 = set1 - set2
print(solo1)

#PASO22
print('----------')
enteros = {1,2,3,4,5}
prod_enteros = 1

for num in enteros:
    prod_enteros *= num
print(prod_enteros)