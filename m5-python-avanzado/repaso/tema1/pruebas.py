vocales = ['a','e','i'] 

vocal = 'o'
if any(letra in vocales for letra in vocal):
    print('La letra', vocal, 'está en la lista de vocales.')
else:
    print('La letra',vocal, 'no está en la lista')