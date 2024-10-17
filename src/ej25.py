'''
Ej 25

Este algoritmo muestra que dia, que mes y en que año has nacido tras introducirlo con 
el siguiente formato: (DD/MM/AAAA)

'''

# Declara una variable con valor / para asegurar que la fecha esta en el formato adecuado
caracter = '/'

# Lee la fecha 
fechaNacimiento = input('Introduce tu fecha de nacimiento (DD/MM/AAAA): ')

# En caso de que la fecha se escriba en el formato correcto
if caracter in fechaNacimiento:
    # Se separa por las /
    partes = fechaNacimiento.split('/')
    # Se imprime el resultado por pantalla
    print(f'Has nacido el mes {partes[0]} el dia {partes[1]} y el año {partes[2]}.')

# Si la fecha no esta en el formato correcto muestra un mensaje de error
else:
    print('Formato incorrecto.')