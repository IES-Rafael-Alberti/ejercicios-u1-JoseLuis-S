capitalInicial = float(input('Introduce el capital a invertir: '))
interes = float(input('Introduce el interes en decimales (3% = 0.03): '))

capitalAño1 = capitalInicial * (interes + 1)
capitalAño2 = capitalAño1 * (interes + 1)
capitalAño3 = capitalAño2 * (interes + 1)

capitalAño1 = round(capitalAño1, 2)
capitalAño2 = round(capitalAño2, 2)
capitalAño3 = round(capitalAño3, 2)

print('Los rendimientos de los primeros 3 años son: ')
print('-Primer año: ' + str(capitalAño1))
print('-Segundo año: ' + str(capitalAño2))
print('-Tercer año: ' + str(capitalAño3))