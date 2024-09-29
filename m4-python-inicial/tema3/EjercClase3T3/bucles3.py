#Pedir una palabra por pantalla
palabra = input('Introduce una palabra: ')

for i in palabra[::-1]:
    print(i)

print()

#Otra opción
for letra in reversed(palabra):
    print(letra)

print()

for i in range(len(palabra)-1,-1,-1):
    print(palabra[i])