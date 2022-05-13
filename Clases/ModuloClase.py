import Clases

rad= int(input("Ingrese un radio > 0 para Círculo: "))

if rad > 0: 
    ObCirculo = Clases.Circulo(int(rad))
    print("El Perímetro es: " + str(ObCirculo.perimetro(ObCirculo.radio)))
    print("El Área es:      " + str(ObCirculo.area(ObCirculo.radio)))
    print()

    rad= int(input("Ingrese un nuevo radio > 0: "))
    print(ObCirculo.setradio(rad))
    print("El Círculo tiene nuevo radio: " + str(ObCirculo.getradio()))
    print()

    #print("Nuevo Círculo")


else:
    print("El Radio debe > 0.")












print(" ")