#Crear dos listas distintas

nombres = ['damian','nayra','celia','mama','david','lucas']

apellidos = ['arellano','dehn', 'rodriguez', 'gutierrez']

frutas = ['pera','manzana', 'platano', 'mango','aguacate','naranja','fresa']

#UNIR DOS LISTAS

#-->Método1
concatenada = nombres + apellidos
concatenada.sort()
#print(concatenada)

#-->Método2
nombres.extend(apellidos)
nombres.sort()
#print(nombres)

#-->Método3
todas = [*nombres,*apellidos,*frutas] #Tener en cuenta --> En el método 2 hemos cambiado el valor original de 'nombres'
todas.sort()
print(todas)

