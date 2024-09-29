def validar_password(password):
    # Comprueba si la contraseña cumple con todos los requisitos
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"
    minusculas_ok = False
    mayusculas_ok = False
    numeros_ok = False
    caracteres_ok = False

    if len(password) >= 8:
        long_ok = True
    else:
        long_ok = False
    
    #Forma que yo conocía 
    for caracter in password:
        if caracter.islower():
            minusculas_ok = True
        elif caracter.isupper():
            mayusculas_ok = True
        elif caracter.isdigit():
            numeros_ok = True
        else:
            caracteres_ok = True

    #Forma de chatGPT - Esta es más comprimida, tener en cuenta
    minusculas_ok = any(letra.islower() for letra in password)
    mayusculas_ok = any(letra.isupper() for letra in password)
    numeros_ok = any(elemento.isnumeric() for elemento in password)
    caracteres_ok = any(elemento in caracteres_especiales for elemento in password)
    
    # Devuelve True si todas las condiciones se cumplen
    return long_ok and minusculas_ok and mayusculas_ok and numeros_ok and caracteres_ok