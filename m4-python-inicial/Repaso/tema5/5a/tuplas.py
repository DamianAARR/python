#PASO1
mi_tupla = (1,2,3)
for elemento in mi_tupla:
    print(elemento)

#PASO2
print('----------')
mi_lista = [1,2,3]
mi_lista[1] = 0
print(mi_lista)

#mi_tupla[1] = 0 --> La tupla es una estructura de datos no modificable

#PASO3
print('----------')
enteros = (1,2,3,4,5,6,7,8,9)
print(sum(enteros))

#PASO4
print('----------')
tupla_strings = ('Home','october','link','action')
lista_letras = []

for elemento in tupla_strings:
    lista_letras.append(elemento[0])

tupla_letras = tuple(lista_letras)
print(tupla_letras)

#PASO5
print('----------')
enteros = (1,2,3,4,5,6,7,8,9)
prod_pares = 1

for num in enteros:
    if num % 2 == 0:
        prod_pares *= num
print(prod_pares)

#PASO6
print('----------')
enteros = (1,2,3,4,5,6,7,8,9)
enteros_desc = enteros[::-1]
print(enteros_desc)

#PASO7
print('----------')
repetidos = (1,2,3,4,5,6,3,2,3,4,2,4,6,7,8,9,6,2,3,4,5,6,7,8,9)
unicos = set(repetidos)
print('unicos:',unicos)

#PASO8
print('----------')
numero = 55
enteros = (1,2,3,4,5,6,7,8,9)

if numero in enteros:
    print(True)
else:
    print(False)

#PASO9
print('----------')
tupla1 = (1,2,3,4,5)
tupla2 = (6,7,8,9,10)
combi = tupla1 + tupla2 #Junta las dos tuplas en una
combi2 = tuple(zip(tupla1,tupla2))
print(combi)
print(combi2)

#PASO10
print('----------')
enteros = (1,2,3,4,5,6,7,8,9)
print(min(enteros))
print(max(enteros))

#PASO11
print('----------')
tupla_strings = ('Home','october','link','action','one','estrepitosamente')
largo = max(tupla_strings, key=len)
corto = min(tupla_strings, key=len)
print('largo:',largo)
print('corto',corto)

#PASO12
print('----------')
nombre = ('Damian',)
revertido = nombre[0][::-1]
print(revertido)

#PASO13
print('----------')
tupla_tuplas = ((1,2),(3,4),(5,6),(7,8))
sumas = []

for elemento in tupla_tuplas:
    sumas.append(sum(elemento))

tupla_sumas = tuple(sumas)
print(tupla_sumas)