'''
Ej 26

Este algoritmo lee una lista de la compra separada por comas y nombra los productos de 1 en 1

'''

# Lee el la lista de la compra separada por comas
listaCompra = input('Introduce tu lista de la compra separada por comas: ')

# La separa por las ,
partes = listaCompra.split(',')

# Imprime la lista 
print("Los productos en tu cesta son:")
# Elimina los espacios que hay entre los productos
for producto in partes:
    print(producto.strip())
    