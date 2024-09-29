#Listas
precios_productos = [30,9.8,42.5,32.6,71.5,44,21.2,53.2,25.3,57.8]
unidades_vendidas = [3,1,0,0,7,2,0,0,4,0]
facturacionTotal = 0

#Bucle para recorrer listas y comprobar facturación por producto
for i in range(0,len(precios_productos)):
    for j in range(0,len(unidades_vendidas)):
        venta = True
        if unidades_vendidas[i] == 0:
            venta = False
    if venta == True:
        facturacionProducto = precios_productos[i] * unidades_vendidas[i]
        #Imprimir facturación por producto
        print('Con el producto',i + 1,'se han facturado',facturacionProducto)
        facturacionTotal = facturacionTotal + facturacionProducto
        facturacionProducto = 0
        
#Imprimir ventas totales y facturación total
print('Cantidad total de ventas:',sum(unidades_vendidas))
print('Facturación total:',facturacionTotal,'euros')