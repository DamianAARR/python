#Pedir por pantalla 4 números al usuario
numeros_usuario = []
terminado = False

while terminado == False:
    numero = input('Introduce un número: ')
    if numero.isnumeric() == False:
        print('No has introducido un número.')
        print()
        continue

    numero = int(numero)

    numeros_usuario.append(numero)

    if len(numeros_usuario) == 4:
        terminado = True

#Ordenar los números en orden ascendente
numeros_ordenados = sorted(numeros_usuario)

#Devolver los números por pantalla
print()
print('El número más alto es',max(numeros_usuario))

print()
print('Números ordenados de forma ascendente:')

for i in numeros_ordenados:
    print(i)

print()
print(numeros_ordenados)
