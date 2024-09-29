#Pedir nombre por pantalla
nombre = input('Introduce tu nombre')
print('Hola',nombre.title())
print('')

#Pedir el dinero por hora y las horas trabajadas en una semana
precio_hora = float(input('Cuánto ganas por hora?'))
horas_semana = float(input('Cuántas horas trabajas a la semana?'))

#Calcular salario semanal y las ganancias anuales
salario_semanal = precio_hora * horas_semana
ganancias_anuales = salario_semanal * 52

#Imprimir por pantalla las ganancias anuales
print('')
print(nombre.title(),'tienes unas ganancias anuales de',ganancias_anuales,'euros')

#Pedir los gastos semanales por pantalla y calcular anuales
print('')
gastos_semanales = float(input('Cuáles son tus gastos semanales?'))
gastos_anuales = gastos_semanales * 52

#Calcular ahorros anualesda
ahorro_anual = ganancias_anuales - gastos_anuales

#Imprimir por pantalla el resultado final
print('')
print(nombre.title(),'tiene un ahorro anual de',ahorro_anual,'euros')

