# Lee el numero de telefono con el formato predeterminado
numeroCompleto = input('Introduce el numero con el siguiente formato (prefijo-numero-extension): ')

# Divide el formato por los -
partes = numeroCompleto.split('-')

# Toma la parte correspondiente al numero de telefono
numero = partes[1]

# Muestra el resultado por pantalla
print(f'El numero telefonico sin prefijo ni extension es: {numero}')