# Funcion SIN PARAMETROS que lee la temperatura en Fahrenheit y la devuelve en Celsius
def cambioCF ():
    tempF = float(input('Introduce la temperatura en grados Fahrenheit: '))
    tempC = ((tempF - 32) * 5) / 9 
    tempC = round(tempC, 2)
    return tempC

# Imprime el resultado en pantalla
print('La temperatura en grados celsius es', cambioCF(),'°C')