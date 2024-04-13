num1= int(input("ingrese un numero: "))
num2= int(input("ingrese un numero: "))

if num1 < num2 :
    for i in range(num1+1,num2):
        print(i)
else:
    for i in range(num1+2,num2):
        print(i)


