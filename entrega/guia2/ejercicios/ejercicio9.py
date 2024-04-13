edad = int(input("Ingrese su edad: "))

if edad >= 18:
    sueldo = float(input("Ingrese su sueldo: "))
    if sueldo >= 100000:
        print("Debe pagar el impuesto")
    else:
        print("No debe pagar el impuesto")
else:
    print("No debes pagar el impuesto")