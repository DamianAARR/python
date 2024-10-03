#Paso1
frutas = ['manzana','platano','pera','higo','frambuesa','fresa']

#Paso2
print(len(frutas))

#Paso3
print(frutas[2])

#Paso4
frutas[1] = 'mora'

#Paso5
frutas.append('mango')

#Paso6
frutas.insert(0,'uva')

#Paso7
for fruta in frutas:
    print(fruta)

#Paso8
ultima_fruta = frutas.pop(-1)

#Paso9
for fruta in frutas:
    print(fruta)

#Paso10
for fruta in frutas:
    print(len(fruta))

#Paso11
for fruta in frutas:
    if len(fruta) > 5:
        print(fruta)

#Paso12
#frutas.remove('cereza') #Da error porque no existe 'cereza'

#Paso13
frutas.clear()
print(frutas)