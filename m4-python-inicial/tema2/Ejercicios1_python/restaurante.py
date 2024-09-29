#Pedir por consola la cantidad consumida de cada plato
ensalada = int(input('Cuantas ensaladas has consumido?'))
sopa = int(input('Cuantas sopas has consumido?'))
dorada = int(input('Cuantas doradas has consumido?'))
arroz = int(input('Cuantss arroce has consumido?'))
lasana = int(input('Cuantas lasana has consumido?'))
brownie = int(input('Cuantss brownie has consumido?'))
helado = int(input('Cuantos helados has consumido?'))
refresco = int(input('Cuantos refrescos has consumido?'))
cafe = int(input('Cuantos cafes has consumido?'))

#Calcular el precio de cada producto y el total
totalEnsalada = ensalada * 12
totalSopa = sopa * 10
totalDorada = dorada * 18
totalArroz = arroz * 14
totalLasana = lasana * 15
totalBrownie = brownie * 8
totalHelado = helado * 6
totalRefresco = refresco * 5.5
totalCafe = cafe * 3.5

totalCuenta = totalEnsalada + totalSopa + totalDorada + totalArroz + totalLasana + totalBrownie + totalHelado + totalRefresco + totalCafe

#Imprimir la cuenta por pantalla
print('El total de la cuenta es', totalCuenta, 'euros')