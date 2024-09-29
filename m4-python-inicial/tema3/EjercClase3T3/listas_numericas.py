#--> Paso 1

numeros = list(range(1,11))
pares = []

#--> Paso 2
numeros_pares = list(range(10,3,-2)) #-->Opción 1

for i in range(0,len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])

pares_invertidos = pares[::-1]

print('--- PASO 2 ---')
print(pares_invertidos)
print()

#--> Paso 3
print('--- PASO 3 ---')

for num in numeros:
    cuadrado = num**2 #Aquí podría poner diréctamente print(num**2)
    print(cuadrado)

#--> Paso 4
print()
print('--- PASO 4 ---')

#2
pares.reverse()
print(pares)

#Versión profe
numeros_pares_invertidos = [numero for numero in numeros if numero % 2 == 0][::-1]
print(numeros_pares_invertidos)

#3
cuadrados = [numeros[i]**2 for i in range(0,len(numeros))]
print(cuadrados)

#Versión profe
numeros_cuadradaos = [numero**2 for numero in numeros]

#--> Paso 5
print()
print('--- PASO 5 ---')

print(min(numeros))
print(numeros[0])

#--> Paso 6
print()
print('--- PASO 6 ---')
print(max(numeros))
print(numeros[-1])

#--> Paso 7
print()
print('--- PASO 7 ---')
suma = 0

for i in range(0,len(numeros)):
    suma = suma + numeros[i]

print(suma)
print(sum(numeros))

#--> Paso 8
print()
print('--- PASO 8 ---')

print(numeros[7])
print(pares[1])

#Version profe

indice_8_original = numeros.index(8)
print(indice_8_original)

indice_8_invertida = numeros_pares_invertidos.index(8)
print(indice_8_invertida)
