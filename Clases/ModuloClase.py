from genericpath import exists
import Clases, os

def pausa():
	print()
	input("Presione Enter para Continuar.")
	os.system("cls")


print()

opcion = 1000
opcion = input()

while opcion != 0:

    print()
    print("      Menú")
    print()
    print("  1 Ingresar r(radio) para crear Círculo.")
    print("  2 Modificar r de Círculo.")
    print("  3 Crear Nuevo Círculo con r = r(Círculo) x n.")
    print()


    opcion = int(input("Elija una opción: "))
    os.system("cls")
    print()

    if opcion == 1:

        rad= int(input("Ingrese un n(número) de r(radio) > 0 para Círculo: "))
        while rad <= 0:
            os.system("cls")
            print("El r debe ser > 0.")
            print()
            rad= int(input("Ingrese un n(número) de r(radio) > 0 para Círculo: "))

        ObCirculo = Clases.Circulo(int(rad))
        os.system("cls")
        print("El Círculo tiene Radio: " + str(ObCirculo.getradio()))
        print("Su Perímetro es: " + str(ObCirculo.perimetro(ObCirculo.radio)))
        print("Su Área es:      " + str(ObCirculo.area(ObCirculo.radio)))
        pausa()
        print()

    elif opcion == 2:
        rad= int(input("Ingrese un nuevo radio > 0: "))
        while rad <= 0:
            os.system("cls")
            print("El r debe ser > 0.")
            print()
            rad= int(input("Ingrese un n(número) de r(radio) > 0 para Círculo: "))
    
        try:
            os.system("cls")
            print(ObCirculo.setradio(rad))
            print("El Círculo tiene nuevo radio: " + str(ObCirculo.getradio()))
            print("Su Nuevo Perímetro es: " + str(ObCirculo.perimetro(ObCirculo.radio)))
            print("Su Nueva Área es:      " + str(ObCirculo.area(ObCirculo.radio)))
            pausa()
            print()
        
        except:
            print("Debe generar 1ro un Círculo")
            pausa()


    elif opcion == 3:
        os.system("cls")
        print("Nuevo Círculo rxn")
        print()
        nro = int(input("Ingrese n > 0 para multiplicar r de nuevo Círculo: "))
        pausa()
        while nro <= 0:
            nro = int(input("Ingrese n > 0 para multiplicar r de nuevo Círculo: "))
        if nro > 0:
            NewCirculo = ObCirculo.NuevoCirculo(nro)
            print("El Nuevo Círculo tiene nuevo Radio: " + str(NewCirculo.getradio()))
            print("Su Nuevo Perímetro es: " + str(NewCirculo.perimetro(NewCirculo.radio)))
            print("Su Nueva Área es:      " + str(NewCirculo.area(NewCirculo.radio)))













"""rad= int(input("Ingrese un n(número) de r(radio) > 0 para Círculo: "))

if rad > 0:


ObCirculo = Clases.Circulo(int(rad))
print("El Círculo tiene Radio: " + str(ObCirculo.getradio()))
print("Su Perímetro es: " + str(ObCirculo.perimetro(ObCirculo.radio)))
print("Su Área es:      " + str(ObCirculo.area(ObCirculo.radio)))
print()

rad= int(input("Ingrese un nuevo radio > 0: "))
pausa()
print(ObCirculo.setradio(rad))
print("El Círculo tiene nuevo radio: " + str(ObCirculo.getradio()))
print("Su Nuevo Perímetro es: " + str(ObCirculo.perimetro(ObCirculo.radio)))
print("Su Nueva Área es:      " + str(ObCirculo.area(ObCirculo.radio)))
print()

print("Nuevo Círculo rxn")
nro = int(input("Ingrese n para multiplicar r de nuevo Círculo: "))
pausa()
if nro > 0:
    NewCirculo = ObCirculo.NuevoCirculo(nro)
    print("El Nuevo Círculo tiene nuevo Radio: " + str(NewCirculo.getradio()))
    print("Su Nuevo Perímetro es: " + str(NewCirculo.perimetro(NewCirculo.radio)))
    print("Su Nueva Área es:      " + str(NewCirculo.area(NewCirculo.radio)))




else:
print("El Radio debe > 0.")"""





