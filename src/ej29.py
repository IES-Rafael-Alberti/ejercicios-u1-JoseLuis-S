# Lee el nombre
nom = input('Introduce tu nombre: ')
# Declara la variable edad como una variable vacia
edad = ''

# Usa un bucle while para obligar al usuario a introducir una edad
while edad is '': 
    edad = int(input('Introduce tu edad: '))

# En caso de que la edad no este comprendida entre 0 y 125 muestra un mensaje de error
if 0 < edad > 125: 
    print('La edad introducida no es valida.')

# En caso de que el usuario no introduzca ningun nombre
elif nom is '':
    # Le asigna el nombre de Desconocido
    nom = 'Desconocido'
    # Calcula la edad restante hasta los 125 años
    edadRestante = 125 - edad
    # Muestra el resultado por pantalla
    print(f'Te llamas {nom} y tienes {edad} años, te quedad aun {edadRestante} años por cumplir.')

# Si ha introducido un nombre y la edad es correcta
else:
    # Calcula la edad restante hasta los 125 años
    edadRestante = 125 - edad
    # Muestra el resultado por pantalla
    print(f'Te llamas {nom} y tienes {edad} años, te quedad aun {edadRestante} años por cumplir.')