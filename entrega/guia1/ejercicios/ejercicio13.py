total = 0
for i in range(10):
    precio = float(input(f"Ingresa el precio del producto {i+1}: "))
    total += precio

promedio = total / 10

print("El promedio de precios de los 10 productos es:", promedio)