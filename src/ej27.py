nomProducto = input('Introduce el nombre del producto: ')
precioProducto = float(input('Introduce el precio total de los productos: '))
numUnidades = float(input('Introduce el numero de unidades: '))

precioUnitario = precioProducto/numUnidades

print(f'{nomProducto} cuesta {precioUnitario: 010.2f}, hay una cantidad de {numUnidades: 03.0f} y todo cuesta {precioProducto: 012.2f}')