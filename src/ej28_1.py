import math

def tiene_mas_de_un_punto(valor: str):
    punto = valor.find('.')
    if punto >= 0 and valor.find('.', punto + 1):
        if valor.find('.', punto + 1):
            return False
        else:
            return True

def comprobar_float(valor: str):
    if valor[:1] == '-':
        valor = valor[1:]

def calcular_area (ladoA, ladoB, ladoC):
    semiperimetro = (ladoA + ladoB + ladoC)/2
    area = math.sqrt( semiperimetro * (semiperimetro - ladoA) * (semiperimetro - ladoB) * (semiperimetro - ladoC))
    return area

def main():
    print('Dime los lados del triangulo: ')

    ladoA = input('Primer lado: ')
    
    ladoB = input('Segundo lado: ')

    ladoC = input('Tercer lado: ')

    print(calcular_area(ladoA, ladoB, ladoC))

# Llama la funcion main
if __name__ == '__main__':
    main()