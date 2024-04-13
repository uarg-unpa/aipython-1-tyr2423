dia = int(input("Ingrese un numero del 1 al 7: "))

if 1 <= dia <= 7:
    dias_semana = {1: "lunes", 2: "martes", 3: "miercoles", 4: "jueves", 5: "viernes", 6: "sabado", 7: "domingo"}
    print(f"El dia que corresponde al numero {dia} es {dias_semana[dia]}")
else:
    print("el numero ingresado no corresponde al rango de [1-7]")