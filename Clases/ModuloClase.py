import Clases

rad= input("Ingrese un Radio > 0: ")

ObCirculo = Clases.Circulo(int(rad))


print(ObCirculo.perimetro(ObCirculo.radio))

print()
rad= input("Ingrese un Radio > 0: ")
print(ObCirculo.setradio(int(rad)))


print(" ")