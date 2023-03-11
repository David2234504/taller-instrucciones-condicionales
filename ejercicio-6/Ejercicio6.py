print("----------------------------")
print("-------Segundo grado--------")
print("----------------------------")


import math

# input
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# processing
discriminante = (b ** 2) - (4 * a * c)

if a == 0:
    print("La ecuación es de la forma lineal")
else:
    if discriminante < 0:
        print("La ecuación no tiene solución real.")
    else:
       x1 = (-b + (math.sqrt(discriminante))) / (2 * a)
       x2 = (-b - (math.sqrt(discriminante))) / (2 * a)
       
       # output
       print("Las soluciones de la ecuación son:")
       print("x1 ="+ str(x1))
       print("x2 ="+ str(x2))