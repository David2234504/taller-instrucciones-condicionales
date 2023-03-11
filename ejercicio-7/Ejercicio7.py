print("-----------------------------------------")
print("-----------Dados tres numeros------------")
print("-----------------------------------------")

#input

a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el valor del tercer numero: "))

# processing
if (a + b) == c: 
    print("La suma de " + str(a) + " mas " + str(b) + " es igual a " + str(c))
 
else:
    print(" La suma de los dos primeros numeros no es quivalente al tercero")