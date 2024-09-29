#Pedir por pantalla la edad
edad = int(input('Cuantos años tienes?: '))

#Pedir cantidad mínima de ingresos para combrobar si aplica
ingreso_minimo = float(input('Cuanto cobras al mes?: '))

#Combrobar si debe tributar
if edad >= 18 and ingreso_minimo > 1000:
    ingresos_anuales = ingreso_minimo * 12
    if ingresos_anuales < 15000:
        print('Te aplica el 5%')
    elif 15000 <= ingresos_anuales <= 25000:
        print('Te aplica el 15%')
    elif 25000 <= ingresos_anuales <= 35000:
        print('Te aplica el 20%')
    elif 35000 <= ingresos_anuales <= 65000:
        print('Te aplica el 20%')
    elif ingresos_anuales > 60000:
        print('Te aplica el 45%')
else:
    print('No tienes que tributar')
