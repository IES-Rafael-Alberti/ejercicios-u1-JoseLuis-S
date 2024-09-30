# Importa la funcion que permite separar con varias opciones
import re

# Declara una variable con los valores ,. para que a posterior se asegure que el precio contiene decimales
caracteres = ',.'

# Lee el precio
precio = input('Introduce el precio del producto (1,00 o 1.00): ')

if caracteres in precio:
    # Separa las partes por las comas y los puntos
    partes= re.split('[.,]', precio)
    # Toma cada parte
    euros = partes[0]
    cents = partes[1]
    # Muestra el resultado por pantalla
    print(f'Has pagado {euros} euros y {cents} centimos.')

# En caso de que el precio no contenga decimales muestra un mensaje de error
else:  
    print('El precio debe contener decimales (1,00 o 1.00).')