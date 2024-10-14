'''
Ej 27

Este algoritmo calcula el precio por unidad de un producto y muestra su nombre,
la cantidad y el precio por unidad

'''

# Lee los datos de nombre de producto, precio total de producto y numero de unidades de producto
nomProducto = input('Introduce el nombre del producto: ')
precioProducto = float(input('Introduce el precio total de los productos: '))
numUnidades = float(input('Introduce el numero de unidades: '))

# Calcula el precio por unidad de producto
precioUnitario = precioProducto/numUnidades

# Imprime el resultado por pantalla
print(f'{nomProducto} cuesta {precioUnitario: 010.2f}, hay una 
      cantidad de {numUnidades: 03.0f} y todo cuesta {precioProducto: 012.2f}')