listaCompra = input('Introduce tu lista de la compra separada por comas: ')

partes = listaCompra.split(',')

print("Los productos en tu cesta son:")
for producto in partes:
    print(producto.lstrip().rstrip())
    