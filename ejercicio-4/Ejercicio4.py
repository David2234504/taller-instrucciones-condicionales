print("---------------------------------")
print("---------Masa Corporal-----------")
print("---------------------------------")

# input
p = float(input("Ingrese el peso en kilogramos: "))
a = float(input("Ingrese la altura en metros: "))

# processing and output
imc = p // (a ** 2)
if imc < 16:
    print("Criterio de ingreso en hospital")
elif 16 < imc < 17:
    print("Infrapeso")
elif 17 < imc < 18:
    print("Bajo peso")
elif 18 < imc < 25:
    print("Peso normal (Saludable)")
elif 25 < imc < 30:
    print("Sobrepeso (Obesidad grado I)")
elif 30 < imc < 35:
    print("Sobrepeso cronico (Obesidad grado II)")
elif 35 < imc < 40:
    print("Obesidad premorbida (obesidad grado III)")
elif 40 < imc:
    print("Obesidad mórbida (obesidad de grado IV)")
else:
    print("Hubo un error con los datos")

