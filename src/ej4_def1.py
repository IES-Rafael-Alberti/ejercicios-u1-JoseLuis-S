def cambioCF ():
    tempF = float(input('Introduce la temperatura en grados Fahrenheit: '))
    tempC = ((tempF - 32) * 5) / 9 
    tempC = round(tempC, 2)
    return tempC

tempF = (cambioCF() * 9/5) + 32
tempF = round(tempF, 2)

print('La temperatura en celsius es', cambioCF(),'°C ' f'({tempF}°F)')

