# Solicitar datos para el rectángulo
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Calcular perímetro y área del rectángulo
perimetro_rectangulo = 2 * (base_rectangulo + altura_rectangulo)
area_rectangulo = base_rectangulo * altura_rectangulo

# Solicitar datos para la circunferencia
radio_circunferencia = float(input("Ingrese el radio de la circunferencia: "))

# Calcular perímetro y área de la circunferencia
perimetro_circunferencia = 2 * 3.14159 * radio_circunferencia
area_circunferencia = 3.14159 * radio_circunferencia ** 2

# Mostrar resultados
print("\nResultados para el rectángulo:")
print("Perímetro:", perimetro_rectangulo)
print("Área:", area_rectangulo)

print("\nResultados para la circunferencia:")
print("Perímetro:", perimetro_circunferencia)
print("Área:", area_circunferencia)