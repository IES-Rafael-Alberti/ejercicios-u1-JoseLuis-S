numeroCompleto = input('Introduce el numero con el siguiente formato (prefijo-numero-extension): ')

partes = numeroCompleto.split('-')

numero = partes[1]

print(f'El numero telefonico sin prefijo ni extension es: {numero}')