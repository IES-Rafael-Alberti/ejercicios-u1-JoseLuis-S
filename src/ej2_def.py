# Funcion para calcular el pago total por las horas trabajadas
def pagoTotal (horas, precioHora):
    total = horas * precioHora
    return total

# Lee las horas y el precio por hora
horas = int(input('Introduce las horas trabajadas: '))
precioHora = int(input('Introduce el precio por hora: '))

# Muestra el resultado por pantalla
print('El total es', pagoTotal(horas, precioHora),'euros.')