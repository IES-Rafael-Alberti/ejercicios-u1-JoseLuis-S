# Define la funcion que calcula la serie Fibonacci hasta el numero introducido
def serieFibonacci(num):
    # Crea una lista llamada serie, con los dos primeros valores de la serie, en
    # la que se iran guardando cada uno de los valores consiguientes
    serie = [0, 1]
    # Mientras la suma de los dos ultimos numeros de la lista sea menor o igual al
    # numero introducido, se sumaran esos valores y se añadira el resultado de la
    # operacion a la lista
    while serie[-1] + serie[-2] <= num: 
        serie.append(serie[-1] + serie[-2])  
    return serie  

# Define la funcion pedirNum, que lee un numero y lo devuelve
def pedirNum():
    # Lee el numero
    num = input('Introduce el numero hasta el que generar la serie Fibonacci: ')
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
    serie = serieFibonacci(num)
    print(f'La serie Fibonacci hasta el numero {num} es: {serie}')

# Ejecuta la funcion main
if __name__ == '__main__':
    main()
