print("-----------------------------------------")
print("-------------Triangulos------------------")
print("-----------------------------------------")

# input
a = float(input("Ingrese la medida del lado a: "))
b = float(input("Ingrese la medida del lado b: "))
c = float(input("Ingrese la medida del lado c: "))

# processing
if a >= c + b or b >= a + c or c >= a + b:
    print("Hay un error con el triangulo")
else:
    if a > b and a > c:
        cateto1 = b
        cateto2 = c
        hipotenusa = a
    elif b > a and b > c:
        cateto1 = a
        cateto2 = c
        hipotenusa = b
    elif c > a and c > b:
        cateto1 = b
        cateto2 = a
        hipotenusa = c

if ((hipotenusa ** 2) == ((cateto1 ** 2)+(cateto2 ** 2))):
        print("El triangulo es recto")
elif ((hipotenusa ** 2) > ((cateto1 ** 2)+(cateto2 ** 2))):
        print("El triangulo es obtuso")
elif ((hipotenusa ** 2) < ((cateto1 ** 2)+(cateto2 ** 2))):
        print("El triangulo es agudo")
