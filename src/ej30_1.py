# Define la funcion comprobarPrimo que comprueba si un numero es primo o no
def comprobarPrimo(num):

    numDivisores = 0

    # Con este bucle for se calcula el numero de divisores,
    # comienza desde el 1 hasta 1 numero menos que el numero
    # introducido
    for i in range (1, num):
            # Si el modulo de la division es 0 se le suma un
            # divisor
            divisores = num % i
            if divisores == 0:
                numDivisores += 1

    # Si tiene mas de 1 divisor (ya que todos los numeros son divisibles
    # entre 1) no es un numero primo y viceversa
    if numDivisores > 1:
        print(f'El numero {num} no es un numero primo.')
    else:
        print(f'El numero {num} es un numero primo.')    

# Define la funcion pedirNum, que lee un numero y lo devuelve
def pedirNum():
    # Lee el numero
    num = input('Introduce el numero entero a comprobar: ')
    # Llama a la funcion comprobar para asegurar que el valor introducido
    # sea un numero
    while not comprobarNum(num):
        num = input('ERROR, introduce un numero: ')
    return int(num)

# Define la funcion comprobarNum que asegura que el numero introducido sea
# un entero natural
def comprobarNum(num: str):
    # Elimina los espacios tras convertir num en str
    num = num.strip()

    # Comprueba que el numero introducido no sea un decimal ni un 
    # numero negativo
    if num.count('.') >= 1 or num.count('-') >= 1 or (num.count('-') == 1 and num[0] != '-'):
        return False

    # Comprueba con un for que los el valor introducido no contenga letras
    for i in num:
        if i not in '0123456789.-':
            return False 
    
    # Comprueba que no se haya dado el valor de un solo -
    if num == '-':
        return False

    return True

# Define la funcion main
def main():
    num = pedirNum()
    comprobarPrimo(num)

# Ejecuta la funcion main
if __name__ == '__main__':
    main()