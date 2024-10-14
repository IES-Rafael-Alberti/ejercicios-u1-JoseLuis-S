'''
Este algoritmo calcula el area de un triangulo, en m o cm, a partir de tres lados
'''

import math

# Define la funcion calcular area que calcula el area en funcion de 3 lados
def calcular_area (ladoA, ladoB, ladoC):
    semiperimetro = (ladoA + ladoB + ladoC)/2
    area = math.sqrt( semiperimetro * (semiperimetro - ladoA) * (semiperimetro - ladoB) * (semiperimetro - ladoC))
    return area

# Define la funcion comprobarNum que comprueba que el numero introducido sea un numero
def comprobarNum(num: str):
    # Elimina los espacios tras convertir num en str
    num = num.strip()

    # Comprueba que el numero no contenga mas de un .- o que no contenga algun - en mitad
    # del numero
    if num.count('.') > 1 or num.count('-') > 1 or (num.count('-') == 1 and num[0] != '-'):
        return False

    # Comprueba con un for que los el valor introducido no contenga letras
    for i in num:
        if i not in '0123456789.-':
            return False 
    
    # Comprueba que no se haya dado el valor de un solo - o .
    if num == '-' or num == '.':
        return False

    return True

# Define la funcion pedirNum, que lee un numero y lo devuelve
def pedirLado(index):
    # En funcion de que lado quiera pedir muestra un mensaje u otro
    mensajes = ["Introduce el primer lado: ", "Introduce el segundo lado: ", "Introduce el tercer lado: "]
    num = input(mensajes[index - 1])
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return float(num)

# Define la funcion pedir_unidad_medida que pide si la unidad es cm o m
def pedir_unidad_medida():
    unidadMedida = input('Introduce la unidad de medida (cm o m): ')

    # Mientras la unidad no sea cm o m seguira pidiendo la unidad
    while unidadMedida != 'cm' and unidadMedida != 'm':
        unidadMedida = input('ERROR, introduce la unidad de medida (cm o m): ')
    return unidadMedida

# Define la funcion pedir_lados_triangulo que pide los lados del triangulo
def pedir_lados_triangulo():

    print('Dime los lados del triangulo: ')

    ladoA = pedirLado(1)
    
    ladoB = pedirLado(2)

    ladoC = pedirLado(3)    

    return ladoA, ladoB, ladoC

# Define la funcion main
def main():

    # Unidad de medida
    unidadMedida = pedir_unidad_medida()

    # Asigna cada valor a cada variable
    ladoA, ladoB, ladoC = pedir_lados_triangulo()

    # Guarda el resultado de la funcion en una variable
    area = calcular_area(ladoA, ladoB, ladoC)

    # Se ajusta la medida al cuadrado
    if unidadMedida == 'cm':
        unidadMedida = 'cm²'
    else:
        unidadMedida = 'm²'

    print(f'El area del triangulo es igual a: {area} {unidadMedida}')

# Llama la funcion main
if __name__ == '__main__':
    main()