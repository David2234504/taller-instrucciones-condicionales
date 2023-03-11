print("----------------------------------------------")
print("-----------Ganancias de papeleria-------------")
print("----------------------------------------------")

# input
c = int(input("Ingrese el valor del costo: "))

#processing and out put
if c < 3000:
    g = c * (15/100) 

elif 3000 < c < 6000:
    g = 500

elif c > 6000:
    g = c * 25/100

p = c + g 

print("El precio total del prodructo es : " + str(p)+"$")
