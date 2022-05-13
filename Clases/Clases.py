"""Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0"""


#                       FORMULAS:

# PERIMETRO
# P = 2pi * Radio           

# AREA
# A = pi * Radio²




class Circulo:

    #ATRIBUTOS

    pi = 3.1416

    def __init__(self,radio):
        print()
        self.radio = radio


    #MÉTODOS

    def setradio(self,radio):
        if radio > 0:
            self.radio = radio
            mensaje = "El radio fue modificado."
            return mensaje

    
    def getradio(self):
        return self.radio


    def perimetro(self,radio):
        if int(radio) <= 0:
            mensaje = "El Radio del ◯  debe ser > 0.   "
            return mensaje
        else:
            perimetro = (2*3.1416) * int(radio)
            return round(perimetro,2)
            

    def area(self,radio):
        if int(radio) <= 0:
            mensaje = "El Radio del ◯  debe ser > 0.  "
            return mensaje
        else:
            area = 3.1416 * (int(radio) * int(radio))
            return round(area,2)

    
    def NuevoCirculo(self,n):
        circulo_rx3 = Circulo(self.radio*n)
        return circulo_rx3


