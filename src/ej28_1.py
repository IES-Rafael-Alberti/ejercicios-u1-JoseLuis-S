import math

def calcular_area (ladoA, ladoB, ladoC):
    semiperimetro = (ladoA + ladoB + ladoC)/2
    area = math.sqrt( semiperimetro * (semiperimetro - ladoA) * (semiperimetro - ladoB) * (semiperimetro - ladoC))
    return area

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

# Define la funcion main
def main():
    print('Dime los lados del triangulo: ')

    ladoA = pedirLado(1)
    
    ladoB = pedirLado(2)

    ladoC = pedirLado(3)

    print(calcular_area(ladoA, ladoB, ladoC))

# Llama la funcion main
if __name__ == '__main__':
    main()