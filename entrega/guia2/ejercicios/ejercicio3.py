contraseña=input("Ingrese una contraseña: ")
contraseña_guardada= contraseña

contraseña_prueba=input("vuelva a ingresar la contraseña: ")

if contraseña_prueba.lower() == contraseña_guardada.lower():
    print("la contraseña ingresada coincide con la guardada")

else:
    print("la contraseña ingresada no coincide con la guardada")
