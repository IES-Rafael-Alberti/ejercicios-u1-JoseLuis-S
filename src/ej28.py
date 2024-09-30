num1 = int(input('Introduce el primer numero entero: '))
num2 = int(input('Introduce el segundo numero entero: '))

if (num1 == num2): 
    print('Los números no pueden ser iguales.')

elif (num1 > num2):
    num3 = num1 - num2
    print(f'El numero {num2} es el menor y entre ellos existen {num3} numeros enteros.')

else:
    num3 = num2 - num1
    print(f'El numero {num1} es el menor y entre ellos existen {num3} numeros enteros.')
