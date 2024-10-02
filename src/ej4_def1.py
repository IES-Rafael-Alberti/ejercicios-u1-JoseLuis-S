# Funcion SIN PARAMETROS que lee la temperatura en Fahrenheit y la devuelve en Celsius
def cambioCF():
    tempF = float(input('Introduce la temperatura en grados Fahrenheit: '))
    tempC = ((tempF - 32) * 5) / 9 
    tempC = round(tempC, 2)
    tempF = round(tempF, 2)
    return 'La temperatura en celsius es {}°C ({})°F'.format(tempC, tempF)

# Define el main y llama la funcion cambio
def main():
    print(cambioCF())

# Llama a la funcion main
if __name__ == '__main__':
    main()
