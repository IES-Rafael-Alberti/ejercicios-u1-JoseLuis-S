# Lee tanto el dividendo como el divisor
n = int(input('Introduce el dividendo de la division: '))
m = int(input('Introduce el divisor de la division: '))

# Calcula el resto y el cociente
c = n//m
r = n%m

# Muestra el resultado por pantalla
print(f'La división de {n} entre {m} da un cociente {c} y un resto {r}')