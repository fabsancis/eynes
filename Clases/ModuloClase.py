import Clases, os
import turtle

def pausa():
	print()
	input("Presione Enter para Continuar.")
	os.system("cls")




opcion = "1000"
#----------------------


while opcion != "0":
    
    print()
    print("      Menú")
    print()
    print("  1 CREAR CÍRCULO.")
    print("  2 MODIFICAR R CÍRCULO.")
    print("  3 MOSTRAR CÍRCULO.")
    print("  4 CREAR NUEVO CIRCULO con r = r(CIRCULO) x n.")
    print("  5 MOSTRAR NUEVO CÍRCULO.")
    print("  0 Salir.")
    print()


    opcion = input("Elija una opción: ")
    print()
    os.system("cls")
    print()


    if opcion == "1":

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


    elif opcion == "2":
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
            print("Debe CREAR CIRCULO primero.")
            pausa()

    
    elif opcion == "3":
        try:
            print()
            os.system("cls")
            print("El Círculo tiene Radio: " + str(ObCirculo.getradio()))
            print("Su Perímetro es: " + str(ObCirculo.perimetro(ObCirculo.radio)))
            print("Su Área es:      " + str(ObCirculo.area(ObCirculo.radio)))
            t = turtle.Turtle()
            radi = ObCirculo.getradio() 
            t.circle(radi)
            pausa()
        except:
            print("Debe CREAR CIRCULO primero.")
            pausa()
        


    elif opcion == "4":
        os.system("cls")
        print("Nuevo Círculo rxn")
        print()
        nro = int(input("Ingrese n > 0 para multiplicar r de nuevo Círculo: "))
    
        while nro <= 0:
            os.system("cls")
            nro = int(input("Ingrese n > 0 para multiplicar r de nuevo Círculo: "))

        try: 
            os.system("cls")
            NewCirculo = ObCirculo.NuevoCirculo(nro)
            print("El Nuevo Círculo tiene nuevo Radio: " + str(NewCirculo.getradio()))
            print("Su Nuevo Perímetro es: " + str(NewCirculo.perimetro(NewCirculo.getradio())))
            print("Su Nueva Área es:      " + str(NewCirculo.area(NewCirculo.getradio())))
            pausa()
        except:
            print("Debe CREAR CIRCULO primero.")
            pausa()

    elif opcion == "5":
        try:
            print()
            os.system("cls")
            print("El Círculo tiene Radio: " + str(NewCirculo.getradio()))
            print("Su Perímetro es: " + str(NewCirculo.perimetro(NewCirculo.getradio())))
            print("Su Área es:      " + str(NewCirculo.area(NewCirculo.getradio())))
            t = turtle.Turtle() 
            radi = NewCirculo.getradio() 
            t.circle(radi)
            pausa()
        except:
            print("Debe CREAR NUEVO CIRCULO primero.")
            pausa()


    elif opcion == "0":
        print("Hasa la próxima!")
    
    else:
        print("Seleccione una opción válida (numérica entre 1 y 3.)")
        pausa()
        





