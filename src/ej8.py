'''
Este algoritmo calcula la suma de tres numeros
'''

# Declara el resultado
resultado = 0

# Suma tres numeros introducidos
for i in range (3):
    num1 = float(input('Introduce un numero: '))
    resultado += num1

# Redondea el resultado a 2 decimales
resultado = round(resultado, 2)

# Muestra el resultado
print(f'La suma de los tres numeros es: {resultado}')