nom = input('Introduce tu nombre: ')
edad = ''

while edad is '': 
    edad = int(input('Introduce tu edad: '))

if 0 < edad > 125: 
    print('La edad introducida no es valida.')
elif nom is '':
    nom = 'Desconocido'
    edadRestante = 125 - edad
    print(f'Te llamas {nom} y tienes {edad} años, te quedad aun {edadRestante} años por cumplir.')
else:
    edadRestante = 125 - edad
    print(f'Te llamas {nom} y tienes {edad} años, te quedad aun {edadRestante} años por cumplir.')