#Inicializar variables y listas
frutas = ['pera','manzana', 'platano', 'mango','aguacate','naranja','fresa']
long = 0
longitudes = []

#Bucle para recorrer lista y comprobar longitud del string
for i in range(0,len(frutas)):
    long = len(frutas[i])
    longitudes.append(long)

#Devolver longitudes de los strings
print(longitudes)
