correoGmail = input('Introduce tu correo Gmail: ')

partes = correoGmail.split('@')

correoCeu = partes[0] 

print(f'Tu nuevo correo es {correoCeu}@ceu.es')

