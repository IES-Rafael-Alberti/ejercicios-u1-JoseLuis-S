# Funcion que compara dos numeros
def compNum(n1,n2):
    if n1 == n2:
        return 0
    if n1 > n2:
        return '{}'.format(n1)
    if n2 > n1:
        return '{}'.format(n2)

# Define main
def main():
    # Pide dos numeros
    n1 = int(input('Introduce el primer numero: '))
    n2 = int(input('Introduce el segundo numero: '))
    # Llama la a la funcion compNum
    if compNum(n1, n2) == 0:
        print('Los numeros introducidos son iguales.')
    else:
        print(compNum(n1, n2), 'es mayor') 

# LLama a la funcion main
if __name__ == '__main__':
    main()
