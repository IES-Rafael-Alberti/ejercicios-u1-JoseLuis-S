# Define la funcion divisoresNum que calcula los divisores de un numero
def divisoresNum(num):
    # Crea una lista para guardar los divisores del numero introducido
    divisores = []
    # Comprueba desde 1 hasta el mismo numero los divisores y los va guardando
    # en la lista divisores
    for i in range (1, num + 1):
        division = num % i 
        if division == 0:
            divisores.append(i)
    return divisores

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
    divisores = divisoresNum(num)
    print(f'Los divisores de {num} son: {divisores}')

# Ejecuta la funcion main
if __name__ == '__main__':
    main()