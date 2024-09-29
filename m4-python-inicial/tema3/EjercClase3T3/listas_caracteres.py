#Crear una lista 

frutas = ['manzana','platanao','cereza','pera','higo','frambuesa','fresa']

frutas[1] = 'mora'

frutas.append('mango') #Por este append mango aparece al final

frutas.insert(0,'uva') #Por este insert uva es la primera fruta

ultima_fruta = frutas.pop() #Con este pop elimino mango de la lista y lo almaceno en 'última_fruta'

frutas.remove('cereza') #Elimina el string 'cereza' de la lista

frutas.clear() #Ahora la lista está vacía

for i in range(0,len(frutas)):
    if len(frutas[i]) > 5:
        print(frutas[i])


