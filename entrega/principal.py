# print("Taller AiPython")

# #argumento posicional
# print("Hola", "Soy", "Jose")
# #argumentos sep y end
# print("hola", "soy", "jose", sep="*", end="\n")
# print("hola", "soy", "jose", end="+")
# print("soy el que sigue")
# print("soy el que no sigue")

# # argumentos posicionales

# print(10, 3.14, "cadena", True)

# edad=int(input("ingrese su edad:"))

# # print ("su edad es"+edad) mal
# print("su edad es", edad)
# print("su edad es"+str(edad))

# edad2=int(input("ingrese su edad:"))
# print(F"su edad es {edad2}")

# num1=3
# num2=4
# print(f"{num1}+{num2}={num1+num2}")
# print(f"{num1}-{num2}={num1-num2}")
# print(f"{num1}*{num2}={num1*num2}")
# print(f"{num1}%{num2}={num1%num2}")
# print(f"{num1}/{num2}={num1/num2}")
# print(f"{num1}//{num2}={num1//num2}")
# print(f"{num1}**{num2}={num1**num2}")


# text="EsTo eS uN texTo MeZclAdO"

# # title
# print(text.title()) #ordena el txt poniendo iniciales en mayus
# print(text)

# texto=text.title()
# print(texto)

# # upper and lower
# print(texto.upper())
# print(texto.lower())

# # replace

# print(texto.replace(" ", "*"))

# print(len(texto))

# sentencia if

# if edad2 > 18:
#     print("ud debe votar")

# print("linea que es independiente del bloque")


# if edad2 >= 18:
#     print("ud debe votar")

# else:
#     print("ud es menor de edad")
# print("linea que es independiente del bloque")

# calificacion= int(input("ingrese calificacion:"))
# if calificacion >=90:
#     print("excelente")
# else:
#     if calificacion >= 80:
#         print("muy bien")
#     else:
#         if calificacion >=70:
#             print("bien")
#         else:
#             print("insuficiente")

# calificacion= int(input("ingrese calificacion:"))
# if calificacion >=90:
#     print("excelente")
# elif calificacion >= 80:
#     print("muy bien")
# elif calificacion >=70:
#     print("bien")
# else:
#     print("insuficiente")


dia= input("Introduce el dia de la semana: ")
match dia:
    case "Lunes":
        print("Hoy es lunes, ¡a trabajar!")
    case "Martes":
        print("Hoy es miercoles, ¡que tengas un buen dia!")
    case "Miercoles":
        print("Hoy es miercoles ¡ya falta poco para el viernes!")
    case "Jueves":
        print("Mañana es viernes!!")
    case "Viernes":
        print("HOY ES")