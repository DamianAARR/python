#Paso1
numeros = [1,2,3,4,5,6,7,8,9,10]

#Paso2
pares1 = []
pares2 = []
for i in range(len(numeros),1,-1):
    if i % 2 == 0:
        pares1.append(i)

print(pares1)

for numero in numeros:
    if numero % 2 == 0:
        pares2.append(numero)

print(pares2[::-1])