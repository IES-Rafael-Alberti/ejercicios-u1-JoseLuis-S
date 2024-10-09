# Importa la biblioteca random
import random

# Define la funcion resultado que tras comparar los dos numeros muestra el resultado
# de colocando el digito menor en primer lugar
def resultado(comparacion, num1, num2, num3):
    if comparacion == False:
        print('Un numero aleatorio entre', num1 ,'y', num2, 'es', numeroRandom(num1, num2))
    else:
        num3 = num1
        num1 = num2
        num2 = num3
        print('Un numero aleatorio entre', num1 ,'y', num2, 'es', numeroRandom(num1, num2))

# Define la funcion comprobarNum que asegura que los numeros introducidos sean float o int
# y no str
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

# Se define la funcion pedirNum1 que da el valor al primer numero
def pedirNum1():
    num = input('Introduce el primer numero: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return float(num)

# Se define la funcion pedirNum2 que da el valor al segundo numero
def pedirNum2():
    num = input('Introduce el segundo numero: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return float(num)

# Se define la funcion comparar_nums que compara ambos numeros y
# devuelve True or False en funcion del resultado
def comparar_nums(num1, num2):
    if num1 > num2:
        return True
    else:
        return False

# Se define la funcion numeroRandom que nos proporciona un numero aleatorio entre 
# los numeros introducidos
def numeroRandom(num1, num2):
    return random.uniform(num1, num2)

# Se define la funcion main y se dan valores a la variables utilizadas
def main():
    num1 = pedirNum1()
    num2 = pedirNum2()
    num3 = 0

    comparacion = comparar_nums(num1, num2)
    resultado(comparacion, num1, num2, num3)

# Llama a la funcion main
if __name__ == '__main__':
    main()