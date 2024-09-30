import re

precio = input('Introduce el precio del producto: ')

partes= re.split('[.,]', precio)

euros = partes[0]
cents = partes[1]

print(f'Has pagado {euros} euros y {cents} centimos.')