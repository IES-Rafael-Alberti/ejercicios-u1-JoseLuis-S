# Define la funcion sumNum que lee un numero n, calcula la suma de todos los enteros hasta n y lo muestra
def sumNum ():
    n = int(input('Introduce un numero entero: '))
    resultado = int((n*(n + 1))/2)
    return 'La suma de todos los enteros desde 1 hasta {} es {}'.format(n, resultado)

# Define la funcion main y llama a sumNum
def main():
    print(sumNum())

# Llama a la funcion main
if __name__ == '__main__':
    main()

