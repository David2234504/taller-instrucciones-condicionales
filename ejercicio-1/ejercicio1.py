print("--------------------------------------")
print("-------------Coordenadas--------------")
print("--------------------------------------")

# input
x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

# processing
if y == 0 and x == 0:
    print("La coordenada esta en el origen")
elif y == 0 and x > 0:
    print("La coordenada esta en el punto "+str(x)+" sobre el eje -y- positivo")
elif y == 0 and x < 0:
    print("La coordenada esta en el punto "+str(x)+" sobre el eje -y- negativo")
elif y > 0 and x == 0:
    print("La coordenada esta en el punto "+str(y)+" sobre el eje -x- positivo")
elif y < 0 and x == 0:
    print("La coordenada esta en el punto "+str(y)+" sobre el eje -x- negativo")
elif y > 0 and x > 0:
    print("La coordenada está en el punto "+str(x)+","+str(y)+" en el primer cuadrante")
elif y > 0 and x < 0:
    print("La coordenada está en el punto "+str(x)+","+str(y)+" en el segundo cuadrante")
elif y < 0 and x < 0:
    print("La coordenada está en el punto "+str(x)+","+str(y)+" en el tercer cuadrante")
elif y < 0 and x > 0:
    print("La coordenada está en el punto "+str(x)+","+str(y)+" en el cuarto cuadrante")
else:
    print("Hubo un error con los datos") 
print("--------------------------------------")

