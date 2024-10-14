'''
Este algoritmo escribe un corremo Gmail en formato @ceu.es 
'''

# Lee el correo a cambiar
correoGmail = input('Introduce tu correo Gmail: ')

# Crea una division tomando como referencia el @
partes = correoGmail.split('@')

# Toma la parte correspondiente al correo
correoCeu = partes[0] 

# Muestra el resultado por pantalla
print(f'Tu nuevo correo es {correoCeu}@ceu.es')

