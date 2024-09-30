fechaNacimiento = input('Introduce tu fecha de nacimiento (DD/MM/AAAA): ')

partes = fechaNacimiento.split('/')

print(f'Has nacido el mes {partes[0]} el dia {partes[1]} y el año {partes[2]}.')