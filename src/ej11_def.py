'''
Este algoritmo calcula la suma de todos los enteros hasta el numero introducido
'''

# Define la funcion sumNum que calcula la suma de todos los enteros hasta un numero
def sumNum (num):
    return int((num*(num + 1))/2)

# Define la funcion main, lee el entero y muestra por pantalla la suma
def main():
    n = int(input('Introduce un numero entero: '))
    print('La suma de todos los enteros desde 1 hasta {} es {}'.format(n, sumNum(n)))

# Llama a la funcion main
if __name__ == '__main__':
    main()

