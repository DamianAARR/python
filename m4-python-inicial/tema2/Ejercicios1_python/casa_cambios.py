#Pedir por consola la cantidad que se va a cambiar
print('Qué cantidad quieres cambiar? (en euros)')
cantidadEuros = input()

valorDolar = 1.2

#Calcular el cambio de euros a dolar, la comisión de la casa y el restante que recibe el usuario
cambioMoneda = int(cantidadEuros) * valorDolar

comisionCasa = cambioMoneda * 0.10

recibeUsuario = cambioMoneda - comisionCasa


#Devolver el resultado de cambiar a dólares
print('Ha introducido ', cantidadEuros, '€ y recibe ', recibeUsuario, '$ ya que la casa se queda con una comisión del 10% (', comisionCasa, '$)' )