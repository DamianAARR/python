#Inicializar variables y listas
frutas = ['pera','manzana', 'platano', 'mango','aguacate','naranja','fresa']
listMayus = []

for i in range(0,len(frutas)):
    listMayus.append(frutas[i].upper())

#Devolver respuesta
print(listMayus)