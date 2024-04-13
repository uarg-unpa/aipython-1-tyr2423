edad=int(input("Ingrese su edad"))
if edad >= 18:
     print("Usted puede conducir")
else:
    años_faltantes= 18 - edad
    print(f"Le faltan {edad} años para poder conducir")
