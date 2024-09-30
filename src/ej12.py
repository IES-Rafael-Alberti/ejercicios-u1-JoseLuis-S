# Lee el peso y la altura 
peso = float(input('Introduce tu peso corporal en kilogramos: '))
altura = float(input('Introduce tu altura en metros: '))

# Calcula el IMC 
imc = peso/altura**2
imc = round(imc, 2)

# Muestra el resultado por pantalla
print(f'Tu índice de masa corporal es: {imc}')