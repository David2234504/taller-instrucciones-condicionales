print("-----------------------------")
print("----Numero n divvisor de m---")
print("-----------------------------")

#input

n = int(input("Digite el primer numeo: "))
m = int(input("Digite el segundo numero: "))


r = n%m 
if r == 0:
    print( str(n) + " es multiplo de " + str(m))

else: 
    print( str(n) + " no es multiplo de " + str(m))


