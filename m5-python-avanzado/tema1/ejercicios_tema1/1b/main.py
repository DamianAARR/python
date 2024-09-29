# Importar módulos
from creador import generar_contrasena as gen_pass
from validador import validar_password

# ---- FUNCIONALIDAD ----

# 1. Solicitar contraseña
pass_user = input('Introduce tu contraseña:\n')

# 2. Llamar a la funcion validadora
validacion = validar_password(pass_user)

if validacion:
    print('Validación correcta')
    print()
else:
    #3. Llamar a la función generadora
    print('Validación incorrecta, se sugiere nueva password')
    new_pass = gen_pass()

    #4. Devolver la contraseña nueva
    print()
    print('Contraseña generada aleatoriamente:',new_pass)
