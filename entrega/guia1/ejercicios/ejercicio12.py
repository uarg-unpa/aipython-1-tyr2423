cantidad_invertir = float(input("Ingresa la cantidad a invertir: "))
interes_anual = float(input("Ingresa el interés anual (en %): "))
num_anios = int(input("Ingresa el número de años: "))

interes_anual /= 100  # Convertir a decimal
capital_final = cantidad_invertir * (1 + interes_anual) ** num_anios

print("El capital obtenido en la inversión es:", capital_final)