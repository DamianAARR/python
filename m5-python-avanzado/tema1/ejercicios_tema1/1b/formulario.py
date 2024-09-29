#Funciones
def validar_formulario(nombre,numero,correo):
    #Comprueba que los datos introducidos son correctos

    name_ok = False
    number_ok = False
    email_ok = False
    
    if len(nombre) >= 3:
        name_ok = True
    
    if numero.isdigit() and len(numero) == 9: #.isnumeric comprueba si los elementos de un string son todos números.
                                                # también se puede usar .isdigit()
        number_ok = True

    if '@' in correo and '.' in correo:
        email_ok = True

    if name_ok and number_ok and email_ok:
        valido = True
    else:
        valido = False
    
    return valido


#Funcionalidad 
nombre = input('Ingrese su nombre:\n')
numero = input('Ingrese su número:\n')
correo = input('Ingrese su correo electrónico:\n')

valido = validar_formulario(nombre,numero,correo)

if valido:
    print('Formulario validado')
else:
    print('Datos introducidos de forma incorrecta')