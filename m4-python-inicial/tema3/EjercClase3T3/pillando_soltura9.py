#Crear lista de números enteros positivos y negativos

lista = [34,54,-3,67,-10,-34,-6,80,4,8,-12,34,90,-23,-65,-76]

positivos = []

#Bucle para recorrer lista y comprobar números positivos
for i in range(0,len(lista)):
    if lista[i] > 0:
        positivos.append(lista[i])

#Devolver respuesta
print(positivos)