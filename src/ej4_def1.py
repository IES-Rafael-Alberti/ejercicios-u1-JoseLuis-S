# Funcion SIN PARAMETROS que lee la temperatura en Fahrenheit y la devuelve en Celsius
def cambioCF ():
    tempF = float(input('Introduce la temperatura en grados Fahrenheit: '))
    tempC = ((tempF - 32) * 5) / 9 
    tempC = round(tempC, 2)
    return tempC

# Invierte la operacion hecha para obtener tempC para volver a obtener tempF y redondea
tempF = (cambioCF() * 9/5) + 32
tempF = round(tempF, 2)

# Muestra el resultado por pantalla
print('La temperatura en celsius es', cambioCF(),'°C ' f'({tempF}°F)')

