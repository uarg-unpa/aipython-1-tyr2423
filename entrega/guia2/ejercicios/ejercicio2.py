mi_edad = 20
tu_edad = int(input("ingrese su edad: "))

if tu_edad > mi_edad:
    diferencia = tu_edad - mi_edad
    if diferencia == 1:
        print(f"Sos mayor que yo por {diferencia} año")
    else:
        print(f"Sos mayor que yo por {diferencia} años")
elif tu_edad < mi_edad:
    diferencia = mi_edad - tu_edad
    if diferencia == 1:
        print(f"Soy mayor que vos por {diferencia} año")
    else:
        print(f"Soy mayor que vos por {diferencia} años")
else:
    print("Ambos tenemos la misma edad") 