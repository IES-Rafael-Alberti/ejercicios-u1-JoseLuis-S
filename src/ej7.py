'''
Este algoritmo calcula la suma de tres numeros
'''

# Entrada de los numeros a operar
num1 = float(input('Introduce el primer numero: ')) 
num2 = float(input('Introduce el segundo numero: ')) 
num3 = float(input('Introduce el tercer numero: ')) 
# Calculo
resultado = num1 + num2 + num3
resultado = round(resultado, 2)

# Muestra el resultado
print(f'El resultado es: {resultado}')