print("--------------------------------------")
print("---------------Prestamo---------------")
print("--------------------------------------")

# input
a = int(input("Ingrese el valor de los ingresos "))
b = int(input("Ingrese cuantas deudas tiene "))

# processing and output
if a > 945200 and b == 0:
    print(" Puede obtener un prestamo de cierto valor")

elif a > 945200 and b > 0:
    print("Tiene los ingresos necesarios pero no se puede acceder al prestamo ya que posee duedas")

elif a < 945200 and b == 0:
    print("No puede accerder al prestamo ya que no posee los ingresos necesarios")
else:
    print("No puede accerder al prestamo ya que no posee los ingresos necesarios y tiene deudas")