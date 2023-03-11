print("---------------------------------")
print("---------Gasto de agua-----------")
print("---------------------------------")

# input
a = float(input("Digite los metros cubicos de agua gastados: "))

# processing
if a <= 50:
    cf = 10000
elif 50 < a < 200:
    cf = ((a - 50) * 2000) + 10000
else:
    cf = ((a - 200) * 3000) + 310000

# output
print("El costo del gasto de agua es de "+str(cf)+"$")