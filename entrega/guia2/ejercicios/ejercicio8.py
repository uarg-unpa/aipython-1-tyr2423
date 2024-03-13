edad= int(input("Ingrese su edad: "))

if edad <= 4:
    print(f"Usted tiene {edad} años por lo tanto su entrada es gratis")
elif 4 <= edad <= 18:
    print(f"Usted tiene {edad} años por lo tanto debe pagar $5")
else:
    print(f"Usted tiene {edad} años por lo tanto debe pagar $10")
