'''
Ej 15

Este algoritmo calcula el interes que obtendras en los proximos 3 años en funcion
del interes y del capital ingresado

'''

# Lee la cantidad inicial y el interes
capitalInicial = float(input('Introduce el capital a invertir: '))
interes = float(input('Introduce el interes en decimales (3% = 0.03): '))

# Calcula el capital con las ganancias por los intereses por año
capitalAño1 = capitalInicial * (interes + 1)
capitalAño2 = capitalAño1 * (interes + 1)
capitalAño3 = capitalAño2 * (interes + 1)

# Redondea los resultados a 2 decimales
capitalAño1 = round(capitalAño1, 2)
capitalAño2 = round(capitalAño2, 2)
capitalAño3 = round(capitalAño3, 2)

print('Los rendimientos de los primeros 3 años son: ')
print(f'-Primer año: {capitalAño1}')
print(f'-Segundo año: {capitalAño2}')
print(f'-Tercer año: {capitalAño3}')