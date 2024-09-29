#Pedir una letra por pantalla
letra = input('Introduce una letra: ')

if letra == letra.lower():
    print()
    print('La letra', letra, 'es minúscula')
    print()
elif letra == letra.upper():
    print()
    print('La letra', letra, 'es mayúscula')
    print()